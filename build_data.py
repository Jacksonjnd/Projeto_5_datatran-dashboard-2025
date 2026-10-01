import pandas as pd, json, math, os
src='/mnt/data/datatran2025.csv'
out='/mnt/data/datatran_dashboard/data.js'
df=pd.read_csv(src, sep=';', encoding='latin1')
# normalize
for c in ['mortos','feridos','feridos_graves','feridos_leves','pessoas','veiculos']:
    df[c]=pd.to_numeric(df[c], errors='coerce').fillna(0).astype(int)
df['data_dt']=pd.to_datetime(df['data_inversa'], errors='coerce')
df['date_int']=df['data_dt'].dt.strftime('%Y%m%d').astype(int)
df['hora_int']=df['horario'].astype(str).str[:2].where(df['horario'].notna(), '00').astype(int)

cat_cols=['dia_semana','uf','municipio','causa_acidente','tipo_acidente','classificacao_acidente','condicao_metereologica','tipo_pista','uso_solo','fase_dia']
dicts={}
code_maps={}
for c in cat_cols:
    vals=sorted(df[c].fillna('Não informado').astype(str).unique().tolist())
    dicts[c]=vals
    code_maps[c]={v:i for i,v in enumerate(vals)}

def code(c,v):
    return code_maps[c][str(v) if pd.notna(v) else 'Não informado']

rows=[]
for r in df.itertuples(index=False):
    br = None if pd.isna(r.br) else int(r.br)
    rows.append([
        int(r.date_int), int(r.hora_int),
        code('dia_semana', r.dia_semana), code('uf', r.uf), br,
        code('municipio', r.municipio), code('causa_acidente', r.causa_acidente),
        code('tipo_acidente', r.tipo_acidente), code('classificacao_acidente', r.classificacao_acidente),
        code('condicao_metereologica', r.condicao_metereologica), code('tipo_pista', r.tipo_pista),
        code('uso_solo', r.uso_solo), code('fase_dia', r.fase_dia),
        int(r.mortos), int(r.feridos), int(r.feridos_graves), int(r.pessoas), int(r.veiculos)
    ])
meta={
    'total_registros':len(df),
    'data_min':df['data_dt'].min().strftime('%Y-%m-%d'),
    'data_max':df['data_dt'].max().strftime('%Y-%m-%d'),
    'gerado_de':'datatran2025.csv'
}
payload={'meta':meta,'dicts':dicts,'rows':rows}
with open(out,'w',encoding='utf-8') as f:
    f.write('window.DASH_DATA=')
    json.dump(payload,f,ensure_ascii=False,separators=(',',':'))
    f.write(';')
print(out, os.path.getsize(out))
