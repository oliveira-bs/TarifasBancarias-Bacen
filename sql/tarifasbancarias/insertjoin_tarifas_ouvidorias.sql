INSERT INTO tarifas.tarifas_ouvidorias(cnpj, nome, codigo, tipo, codigo_servico, 
servico, unidade, data_vigencia, valor_maximo, tipo_valor, periodicidade, 
ouvidor, website, telefone)
select ti.cnpj, ti.nome, ti.codigo, ti.tipo, ti.codigo_servico, ti.servico, 
ti.unidade, ti.data_vigencia, ti.valor_maximo, ti.tipo_valor, ti.periodicidade, 
o.ouvidor, o.website, o.telefone 
from tarifas.tarifas_instituicoes as ti
inner join tarifas.ouvidorias as o
on ti.cnpj = o.cnpj;
