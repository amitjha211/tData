
GO

alter table trTrade
	add isModified bit 
GOTO
alter table tOrderbook
	add segment varchar(100) 
GO



ALTER view [dbo].[vOrderBook]
as

with tOrderTag 
as
(
	select order_id
	,SUM(qty_adj) as qty_adj 
	from trReduceOrder group by order_id
)

select 
	tOrderBook.*
	,tOrderTag.qty_adj
	,tOrderBook.qty - isnull(tOrderTag.qty_adj,0) as qty_bal
	,day_count = datediff(day,tOrderBook.trade_date,getdate())
	,expiryInDays = DATEDIFF(DAY,GETDATE(),expiryDate)
    ,expiryYear   = Year(expiryDate)
    ,expiryMonth   = Month(expiryDate)
	,tOrderBook.price * (tOrderBook.qty - isnull(tOrderTag.qty_adj,0)) as amount_bal 
	,tOrderBook_Flag.flag
	,tOrderBook_Flag.flag_info
from  
	tOrderBook left join tOrderTag on tOrderBook.order_id = tOrderTag.order_id
				left join tOrderBook_Flag on tOrderBook.order_id = tOrderBook_Flag.order_id
				
GO