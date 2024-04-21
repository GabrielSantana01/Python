SELECT        hist01.[SIGLA] COLLATE Latin1_General_CI_AS AS SIGLA, hist01.[% TOTAL] AS '%TOTAL', QTD.[QUANTIDADE TOTAL] AS 'QTD TOTAL PTS', SUM(QTD.[QUANTIDADE NULL] + QTD.[QUANTIDADE BAD] + QTD.[QUANTIDADE <0]) 
                         AS 'BAD'
FROM            dbo.Analise_Porcentagem_TAGs AS hist01 INNER JOIN
                         dbo.Analise_Quantidade_TAGs AS QTD ON hist01.SIGLA = QTD.[SIGLA]



SELECT        hist02.SIGLA AS SIGLA, hist02.[% TOTAL] AS '%TOTAL', QTD2.[QUANTIDADE TOTAL] AS 'QTD TOTAL PTS', SUM(QTD2.[QUANTIDADE NULL] + QTD2.[QUANTIDADE BAD] + QTD2.[QUANTIDADE <0]) AS 'BAD'
FROM            [HISTORIAN02-EVT].[Runtime].dbo.Analise_Porcentagem_TAGs AS hist02 INNER JOIN
                         [HISTORIAN02-EVT].[Runtime].dbo.Analise_Quantidade_TAGs AS QTD2 ON hist02.SIGLA = QTD2.[SIGLA]
WHERE        (hist02.SIGLA <> 'tstam') AND (hist02.SIGLA <> 'vazao') AND (hist02.SIGLA <> 'schedule') AND (hist02.SIGLA <> 'temp') AND (hist02.SIGLA <> 'ClimaTempo') AND (hist02.SIGLA <> 'VOCA') AND (hist02.SIGLA <> 'AMRBP')
GROUP BY hist02.SIGLA, hist02.[% TOTAL], QTD2.[QUANTIDADE TOTAL]
GO

Analise_Quantidade_tags
-------------------------------------------------------------------------------------------------------------------------------
SELECT     dbo.AllTags_QuantidadeTotal.SIGLA, ISNULL(CAST(dbo.AllTags_QuantidadeTotal.[QUANTIDADE TOTAL] AS decimal(20, 2)), 0) AS [QUANTIDADE TOTAL], 
                      ISNULL(CAST(dbo.AllTags_QuantidadeNull.[QUANTIDADE NULL] AS decimal(20, 2)), 0) AS [QUANTIDADE NULL], 
                      ISNULL(CAST(dbo.AllTags_QuantidadeBAD.[QUANTIDADE BAD] AS decimal(20, 2)), 0) AS [QUANTIDADE BAD], 
                      ISNULL(CAST(dbo.AllTags_Quantidade0.[QUANTIDADE <0] AS decimal(20, 2)), 0) AS [QUANTIDADE <0]
FROM         dbo.AllTags_QuantidadeTotal LEFT OUTER JOIN
                      dbo.AllTags_Quantidade0 ON dbo.AllTags_QuantidadeTotal.SIGLA = dbo.AllTags_Quantidade0.SIGLA LEFT OUTER JOIN
                      dbo.AllTags_QuantidadeBAD ON dbo.AllTags_QuantidadeTotal.SIGLA = dbo.AllTags_QuantidadeBAD.SIGLA LEFT OUTER JOIN
                      dbo.AllTags_QuantidadeNull ON dbo.AllTags_QuantidadeTotal.SIGLA = dbo.AllTags_QuantidadeNull.SIGLA
WHERE     (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%AppServer%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%ClimaTempo%') AND 
                      (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%Develop%') AND 
                      (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%Disponibilidade%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%Envio%') AND 
                      (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%EVERTICAL01%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%GRHistorian01%') AND 
                      (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%Operacao%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%Workflow%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%tstam%') AND
					  (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%vmaua%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%vazao%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%schedule%') AND (dbo.AllTags_QuantidadeTotal.SIGLA NOT LIKE N'%temp%') 

GO
---------------------------------------------------------------------------------------------------------------------------------------------

SELECT T1.[SIGLA],T1.[QTD TOTAL PTS], T1.BAD, ISNULL(T2.[QUANTIDADE PONTOS], 0) AS NULLGR,  (T1.BAD - ISNULL(T2.[QUANTIDADE PONTOS], 0)) AS NULLREAL, ((T1.BAD - ISNULL(T2.[QUANTIDADE PONTOS], 0))*100)/T1.[QTD TOTAL PTS] AS PorcReal
FROM [Runtime].[dbo].[View_Estatistica_Disponibilidade] AS T1
LEFT JOIN  [Runtime].[dbo].[AllTags_QuantidadeNullGR] AS T2
ON T1.SIGLA = T2.SIGLA
order by T1.[SIGLA]
----------------------------------------------------------------------------------------------------------------------------------------------------
select TagName COLLATE Latin1_General_CI_AS as tagname
FROM [Runtime].[dbo].[AllTags_Live] 
except
SELECT     objeto.tag_name +'.'+ atributo.attribute_name as TagName
FROM         [GR01-EVT].[EVERTICAL2].[dbo].[gobject] as objeto 
INNER JOIN [GR01-EVT].[EVERTICAL2].[dbo].[dynamic_attribute] AS atributo
ON objeto.gobject_id = atributo.gobject_id
where atributo.mx_primitive_id = 100 and atributo.mx_data_type < 16
-------------------------------------------------------------------------------------------
[Analise_Porcentagem_TAGs] e [Analise_Quantidade_TAGs] que alimenta a [View_Estatistica_Disponibilidade] responsavel por exibir a porcentagem total dos pontos fora e sua quantidade
[Disponibilidade_porcentagem] alimenta a [View_comparacao_Porcentagem_TAGs] que determina qual predio esta com indisponibilidade maior que 65%
[Disponibilidade_porcentagem] é alimentado por [View_Estatistica_Disponibilidade] e [AllTags_QuantidadeNullGR] = ele verifica as porcentagens vinda do GR01
subitraindo da quantidade real de disponibilidade tudo que esta no Historian e nao esta no GR.

[AllTags_QuantidadeNullGR] é uma reorganização de [def_GRxhist] onde é feito uma contagem dos pontos que existe no HIstorian mas nao existe no GR
[def_GRxhist] = é de fato a query que verifica os itens que existe em alltags_live e nao existe no GR