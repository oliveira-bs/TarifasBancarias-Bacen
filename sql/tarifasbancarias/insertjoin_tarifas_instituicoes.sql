INSERT INTO tarifas.tarifas_instituicoes(cnpj, nome, codigo, tipo, codigo_servico, 
servico, unidade, data_vigencia, valor_maximo, tipo_valor, periodicidade)
select inst.cnpj, inst.nome, g.codigo, g.tipo, t.codigo_servico, t.servico, 
t.unidade, t.data_vigencia, t.valor_maximo, t.tipo_valor, t.periodicidade 
from tarifas.grupos as g
inner join tarifas.instituicoes as inst
on inst.codigo = g.codigo
inner join tarifas.tarifas as t
on inst.cnpj = t.cnpj;
