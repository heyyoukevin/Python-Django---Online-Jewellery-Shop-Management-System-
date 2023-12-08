from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

from jeweapp.forms import pform
from jeweapp.models import pmodel
from  datetime import date 
from datetime import datetime
now = date.today()
today1=date.today()
import datetime
today_date = datetime.date.today()
today = today_date.strftime("%Y-%m-%d")




def  home(request):
	return render(request,'index.html')




def  customer(request):
	return render(request,'customer.html')
	
def customeraction(request):
	cur=connection.cursor()
	ctn=request.GET['name']
	chn=request.GET['housename']
	str=request.GET['street']
	ct=request.GET['city']
	dt=request.GET['district']
	pn=request.GET['pincode']
	ph=request.GET['phno']
	eml=request.GET['emailid']
	ps=request.GET['password']
	sql="insert into customer(ctname,chname,street,city,dist,pin,phno,eml,status)  values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(ctn,chn,str,ct,dt,pn,ph,eml,'Active')
	cur.execute(sql)
	sq="select max(cid)  from customer"
	cur.execute(sq)
	result=cur.fetchall()
	list=[]
	for row in result:
		uid=row[0]
	emailsql="insert into login(uid,uname,upass,utype,status) values('%s','%s','%s','%s','%s')" %(uid,eml,ps,'customer','true')
	cur.execute(emailsql)
	h="<script>alert('NEW CUSTOMER IS SUCCESSFULLY ADDED');window.location='/login/';</script>"
	return HttpResponse(h)
	
def viewcustomer(request):
	cur=connection.cursor()
	s="select * from customer"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'cid':row[0],'ctname':row[1],'chname':row[2],'street':row[3],'city':row[4],'dist':row[5],'pin':row[6],'phno':row[7],'eml':row[8],'status':row[9]}
		list.append(w)
	return render(request,'viewcustomer.html',{'list':list})
	
def uactivate(request):
	cur=connection.cursor()
	cn=request.GET['n']
	st=request.GET['st']
	st1=request.GET['st1']
	s="update customer  set status='%s' where cid='%s'"%(st,cn)
	cur.execute(s)
	s1="update login set status='%s' where uid='%s' and utype='customer'"%(st1,cn)
	cur.execute(s1)
	h="<script>alert(' DETAILS ARE SUCCESSFULLY UPDATED');window.location='/viewcustomer/';</script>"
	return HttpResponse(h)




def login(request):
	return render(request,'login.html')

def searchlogin(request):
	cursor=connection.cursor()
	p=request.POST['username']
	q=request.POST['password']
	sql2="select * from login where uname='%s' and upass='%s' and status='true' " %(p,q)
	cursor.execute(sql2)
	result=cursor.fetchall()
	if	(cursor.rowcount) > 0:
		sql3 = "select * from login where uname='%s' and upass='%s' and status='true'  " % (p,q)
		cursor.execute(sql3)
		result1=cursor.fetchall()
		for row1 in result:
			request.session['uid'] = row1[0]
			request.session['uname'] =row1[1]
			request.session['upass'] = row1[2]
			request.session['utype'] =row1[3]
		if(request.session['utype']=='admin'):
			return render(request,'adminhome.html')
		elif(request.session['utype']=='customer'):
			return render(request,'customerhome.html')
		elif(request.session['utype']=='staff'):
			return render(request,'staffhome.html')
		else:
			html="<script>alert('YOU ENTERED INVALID PASSWORD AND USERNAME');window.location='/home/';</script>"
			return HttpResponse(html)
	else:
		html="<script>alert('YOU ENTERED INVALID PASSWORD AND USERNAME');window.location='/home/';</script>"
		return HttpResponse(html)	
	
	
	
	
def  adminhome(request):
	return render(request,'adminhome.html')	
	
	
	
	
def  category(request):
	list=vcat(request)
	return render(request,'category.html',{'list':list})
	
def categoryaction(request):
	cur=connection.cursor()
	cn=request.GET['catname']
	ds=request.GET['description']
	sql="insert into category(cname,descp)  values('%s','%s')" %(cn,ds)
	cur.execute(sql)
	h="<script>alert('NEW CATEGORY IS SUCCESSFULLY INSERTED');window.location='/category/';</script>"
	return HttpResponse(h)
	
def viewcategory(request):
	cur=connection.cursor()
	list=vcat(request)
	return render(request,'viewcategory.html',{'list':list})
	
def delcat(request):
	cursor=connection.cursor()
	n=request.GET['n']
	sql="delete from category where cname='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('CATEGORY DELETED SUCCESSFULLY');window.location='/category/';</script>"
	return HttpResponse(h)
	 
def editcat(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from category where cname='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'cname':row[0],'descp':row[1]}
		list.append(w)
	return render(request,'editcat.html',{'list':list})
	
def updatecat(request):
	cur=connection.cursor()
	cn=request.GET['catname']
	dn=request.GET['description']
	s="update category set descp='%s' where cname='%s'"%(dn,cn)
	cur.execute(s)
	h="<script>alert('CATEGORY DETAILS ARE SUCCESSFULLY UPDATED');window.location='/category/';</script>"
	return HttpResponse(h)
		
	
	
	
def  subcategory(request):
	list=vscat(request)
	return render(request,'subcategory.html',{'list':list})
	
def subcategoryaction(request):
	cur=connection.cursor()
	scn=request.GET['subcatname']
	ds=request.GET['description']
	sql="insert into subcategory(scname,descp)  values('%s','%s')" %(scn,ds)
	cur.execute(sql)
	h="<script>alert('NEW SUBCATEGORY IS SUCCESSFULLY INSERTED');window.location='/subcategory/';</script>"
	return HttpResponse(h)
	
def viewsubcategory(request):
	cur=connection.cursor()
	list=vscat(request)
	return render(request,'viewsubcategory.html',{'list':list})
	
def delsubcat(request):
	cursor=connection.cursor()
	n=request.GET['n']
	sql="delete from subcategory where scatid='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('SUBCATEGORY DELETED SUCCESSFULLY');window.location='/subcategory/';</script>"
	return HttpResponse(h)
	
def editsubcat(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from subcategory where scatid='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'scatid':row[0],'scname':row[1],'descp':row[2]}
		list.append(w)
	return render(request,'editsubcat.html',{'list':list})
	
def updatesubcat(request):
	cur=connection.cursor()
	scid=request.GET['subcatid']
	scn=request.GET['subcatname']
	dcn=request.GET['description']
	s="update subcategory set scname='%s',descp='%s' where scatid='%s'"%(scn,dcn,scid)
	cur.execute(s)
	h="<script>alert('SUBCATEGORY DETAILS ARE SUCCESSFULLY UPDATED');window.location='/subcategory/';</script>"
	return HttpResponse(h)



	
def  rate(request):
	if (request.method == 'GET' and 'd1' in request.GET):
		s="select * from rate where  rdate='%s' order by rid desc"%(request.GET['d1'])
		list=vrate(s)
	else:
		s="select * from rate  order by rid desc"
		list=vrate(s)
		list1=vcat(request)
	return render(request,'rate.html',{'list':list,'list1':list1,'today':today})
	
def rateaction(request):
	cur=connection.cursor()
	cn=request.GET['category']
	rd=request.GET['date']
	r=request.GET['rate']
	sql="insert into rate(cname,rdate,rate)  values('%s','%s','%s')" %(cn,rd,r)
	cur.execute(sql)
	h="<script>alert('NEW RATE IS SUCCESSFULLY INSERTED');window.location='/rate/';</script>"
	return HttpResponse(h)
	
def viewrate(request):
	if (request.method == 'GET' and 'd1' in request.GET):
		s="select * from rate where  rdate='%s' order by rid desc"%(request.GET['d1'])
		list=vrate(s)
	else:
		s="select * from rate  order by rid desc"
		list=vrate(s)
	return render(request,'viewrate.html',{'list':list})
	
def delrate(request):
	cursor=connection.cursor()
	n=request.GET['n']
	sql="delete from rate where rid='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('RATE DELETED SUCCESSFULLY');window.location='/rate/';</script>"
	return HttpResponse(h)
	
def editrate(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from rate where rid='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'rid':row[0],'cname':row[1],'rdate':row[2],'rate':row[3]}
		list.append(w)
	return render(request,'editrate.html',{'list':list})
	
def updaterate(request):
	cur=connection.cursor()
	rid=request.GET['rid']
	rd=request.GET['date']
	r=request.GET['rate']
	s="update rate set rdate='%s',rate='%s' where rid='%s'"%(rd,r,rid)
	cur.execute(s)
	h="<script>alert('RATE DETAILS ARE SUCCESSFULLY UPDATED');window.location='/rate/';</script>"
	return HttpResponse(h)




def item(request):
	list=vcat(request)
	list1=vscat(request)
	list2=vitem(request)
	return render(request,'item.html',{'list':list,'list1':list1,'list2':list2})
	
def itemaction(request):
    if request.method == "POST":
        MyProfileForm = pform(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile =pmodel()
			
            profile.iname =MyProfileForm.cleaned_data["iname"]
            profile.cname = request.POST["category"]
            profile.scname = request.POST["subcategory"]
            profile.modal = request.POST["modal"]
            profile.wght = request.POST["weight"]			
            profile.stonedtl =request.POST["stonedetails"]
            profile.swght =request.POST["stoneweight"]
            profile.sprice = request.POST["stoneprice"]
            profile.mcharge = request.POST["makingcharge"]
            profile.size = request.POST["size"]
            profile.descp = request.POST["description"]
            profile.p_image = MyProfileForm.cleaned_data["p_image"]
            profile.qty =0
            profile.save()
            html = "<script>alert('NEW ITEM IS SUCCESSFULLY INSERTED');window.location='/item/';</script>"
            saved = True
	else:
		MyProfileForm = pform()
	return HttpResponse(html)
	
def viewitem(request):
	cur=connection.cursor()
	list=vitem(request)
	return render(request,'itemview.html',{'list':list})
	
def delprod(request):
	cursor=connection.cursor()
	n=request.GET['n']
	sql="delete from item where icode='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('ITEM DELETED SUCCESSFULLY');window.location='/item/';</script>"
	return HttpResponse(h)
	
def editprod(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from item where icode='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'icode':row[0],'iname':row[1],'cname':row[2],'scname':row[3],'modal':row[4],'wght':row[5],'stonedtl':row[6],'swght':row[7],'sprice':row[8],'mcharge':row[9],'size':row[10],'descp':row[11],'p_image':row[12],'qty':row[13]}
		list.append(w)
	return render(request,'editprod.html',{'list':list})
	
def updateprod(request):
	cur=connection.cursor()
	icd=request.GET['icode']
	inm=request.GET['iname']
	md=request.GET['modal']
	wgt=request.GET['weight']
	sdt=request.GET['stonedetails']
	swgt=request.GET['stoneweight']
	spr=request.GET['stoneprice']
	mcr=request.GET['makingcharge']
	sz=request.GET['size']
	dcp=request.GET['description']
	s="update item set iname='%s',modal='%s',wght='%s',stonedtl='%s',swght='%s',sprice='%s',mcharge='%s',size='%s',descp='%s' where icode='%s'"%(inm,md,wgt,sdt,swgt,spr,mcr,sz,dcp,icd)
	cur.execute(s)
	h="<script>alert('ITEM DETAILS ARE SUCCESSFULLY UPDATED');window.location='/item/';</script>"
	return HttpResponse(h)




def  staff(request):
	list=vstaff(request)
	return render(request,'staff.html',{'list':list})
	
def staffaction(request):
	cur=connection.cursor()
	stn=request.GET['name']
	shn=request.GET['housename']
	str=request.GET['street']
	ct=request.GET['city']
	dt=request.GET['district']
	pn=request.GET['pincode']
	st=request.GET['state']
	ph=request.GET['phno']
	eml=request.GET['emailid']
	ps=request.GET['password']
	sql="insert into staff(stfname,shname,street,city,dist,pin,state,phno,eml,status)  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(stn,shn,str,ct,dt,pn,st,ph,eml,'Active')
	cur.execute(sql)
	sq="select max(stfid) as uid from staff"
	cur.execute(sq)
	result=cur.fetchall()
	list=[]
	for row in result:
		uid=row[0]
	emailsql="insert into login(uid,uname,upass,utype,status) values('%s','%s','%s','%s','%s')" %(uid,eml,ps,'staff','true')
	cur.execute(emailsql)
	h="<script>alert('NEW STAFF IS SUCCESSFULLY ADDED');window.location='/staff/';</script>"
	return HttpResponse(h)
	
def viewstaff(request):
	cur=connection.cursor()
	list=vstaff(request)
	return render(request,'viewstaff.html',{'list':list})
	
def editstaff(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from staff where stfid='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'stfid':row[0],'stfname':row[1],'shname':row[2],'street':row[3],'city':row[4],'dist':row[5],'pin':row[6],'state':row[7],'phno':row[8],'eml':row[9]}
		list.append(w)
	return render(request,'editstaff.html',{'list':list})
	
def updatestaff(request):
	cur=connection.cursor()
	stfid=request.GET['stfid']
	n=request.GET['name']
	hn=request.GET['housename']
	strt=request.GET['street']
	ct=request.GET['city']
	dst=request.GET['district']
	pn=request.GET['pincode']
	st=request.GET['state']
	ph=request.GET['phno']
	s="update staff set stfname='%s',shname='%s',street='%s',city='%s',dist='%s',pin='%s',state='%s',phno='%s' where stfid='%s'"%(n,hn,strt,ct,dst,pn,st,ph,stfid)
	cur.execute(s)
	h="<script>alert('STAFF DETAILS ARE SUCCESSFULLY UPDATED');window.location='/staff/';</script>"
	return HttpResponse(h)
	
def sactivate(request):
	cur=connection.cursor()
	cn=request.GET['n']
	st=request.GET['st']
	st1=request.GET['st1']
	s="update staff  set status='%s' where stfid='%s'"%(st,cn)
	cur.execute(s)
	s1="update login set status='%s' where uid='%s' and utype='staff'"%(st1,cn)
	cur.execute(s1)
	h="<script>alert(' DETAILS ARE SUCCESSFULLY UPDATED');window.location='/staff/';</script>"
	return HttpResponse(h)




def  vendor(request):
	list=vvendor(request)
	return render(request,'vendor.html',{'list':list,'utype':request.session['utype']})
	
def vendoraction(request):
	cur=connection.cursor()
	vn=request.GET['vendorname']
	on=request.GET['ownername']
	adr=request.GET['address']
	ct=request.GET['city']
	dist=request.GET['district']
	st=request.GET['state']
	pin=request.GET['pincode']
	eml=request.GET['emailid']
	ph=request.GET['phoneno']
	sql="insert into vendor(vname,oname,adrs,city,dist,state,pin,eml,phno)  values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(vn,on,adr,ct,dist,st,pin,eml,ph)
	cur.execute(sql)
	h="<script>alert('NEW VENDOR IS SUCCESSFULLY INSERTED');window.location='/vendor/';</script>"
	return HttpResponse(h)
	
def viewvendor(request):
	cur=connection.cursor()
	list=vvendor(request)
	return render(request,'viewvendor.html',{'list':list,'utype':request.session['utype']})
	
def delvendr(request):
	cursor=connection.cursor()
	n=request.GET['n']
	sql="delete from vendor where vid='%s'"%(n)
	cursor.execute(sql)
	h="<script>alert('VENDOR DELETED SUCCESSFULLY');window.location='/vendor/';</script>"
	return HttpResponse(h)
	
def editvendor(request):
	cur=connection.cursor()
	id=request.GET['n']
	s="select * from vendor where vid='%s'"%(id)
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'vid':row[0],'vname':row[1],'oname':row[2],'adrs':row[3],'city':row[4],'dist':row[5],'state':row[6],'pin':row[7],'eml':row[8],'phno':row[9]}
		list.append(w)
	return render(request,'editvendor.html',{'list':list})
	
def updatevendor(request):
	cur=connection.cursor()
	vid=request.GET['vid']
	vn=request.GET['vendorname']
	on=request.GET['ownername']
	adr=request.GET['address']
	ct=request.GET['city']
	dst=request.GET['district']
	st=request.GET['state']
	pn=request.GET['pincode']
	phn=request.GET['phoneno']
	s="update vendor set vname='%s',oname='%s',adrs='%s',city='%s',dist='%s',state='%s',pin='%s',phno='%s' where vid='%s'"%(vn,on,adr,ct,dst,st,pn,phn,vid)
	cur.execute(s)
	h="<script>alert('VENDOR DETAILS ARE SUCCESSFULLY UPDATED');window.location='/vendor/';</script>"
	return HttpResponse(h)




def  purchasemaster(request):
	cursor = connection.cursor()
	if(request.session['utype']=='admin'):
		sql2="select purchasemaster.pid,purchasemaster.dop,purchasemaster.tamt,vendor.vname from purchasemaster  inner join vendor on purchasemaster.vid=vendor.vid "
    
	elif(request.session['utype']=='staff'):
		sql2="select purchasemaster.pid,purchasemaster.dop,purchasemaster.tamt,vendor.vname from purchasemaster  inner join vendor on purchasemaster.vid=vendor.vid where purchasemaster.stfid='%s'"%(request.session['uid'])
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {'pid' : row[0],'pdate': row[1],'tamt':row[2],'vid':row[3]}
		list.append(w)
	list2=vvendor(request)
	return render(request,'purchasemaster.html', {'list1': list,'list2':list2,'utype':request.session['utype'],'today':today})	
	
def purchasemasteraction(request):
	cur=connection.cursor()
	vn=request.GET['vendor']
	dp=request.GET['purchasedate']
	stf=request.session['uid']
	sql="insert into purchasemaster(vid,dop,stfid,tamt)  values('%s','%s','%s','%s')" %(vn,dp,stf,0)
	cur.execute(sql)
	h="<script>alert('SUCCESSFULLY INSERTED');window.location='/purchasemaster/';</script>"
	return HttpResponse(h)
	
def viewpurchasemaster(request):
	cur=connection.cursor()
	s="select * from purchasemaster"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'pid':row[0],'vid':row[1],'dop':row[2],'stfid':row[3],'tqty':row[4]}
		list.append(w)
	return render(request,'viewpurchasemaster.html',{'list':list})



	
def  purchasechild(request):
    cursor = connection.cursor()
    pmid=request.GET['pid']
    sql2="select purchasechild.*,item.iname from purchasechild inner join item on purchasechild.icode=item.icode where pid='%s'"%(pmid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    for row in result:
        w = {'pcid' : row[0],'pid': row[1],'icode':row[2],'qty':row[3],'amt':row[4],'tamt':row[5],'iname':row[6]}
        list.append(w)
    list2=vitem(request)
    return render(request,'purchasechild.html', {'list1': list,'list2':list2,'pmid':pmid,'utype':request.session['utype']})
	
def purchasechildaction(request):
    cursor=connection.cursor()
    pmid=request.GET['t0']
    bid=request.GET['itemcode']
    qty=request.GET['quantity']
    uamt=request.GET['amount']
    tamt=int(qty)*int(uamt)
    sql="insert into purchasechild(pid,icode,qty,amt,tamt) values('%s','%s','%s','%s','%s')"%(pmid,bid,qty,uamt,tamt)
    #return HttpResponse(sql)
    cursor.execute(sql)
    sql2="select tamt from purchasemaster where pid='%s'"%(pmid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    for row in result:
        pm=row[0]
	pmn=int(pm)+tamt
    sql4="select qty from item where icode='%s'"%(bid)
    cursor.execute(sql4)
    #return HttpResponse(sql4)
    result3=cursor.fetchall()
    for row3 in result3:
        bqty1=int(row3[0])
    bqty=bqty1+int(qty)
    sql3="update purchasemaster set tamt='%s'  where pid='%s'"%(pmn,pmid)
    cursor.execute(sql3)
    sql5="update item set qty='%s'  where icode='%s'"%(bqty,bid)
    cursor.execute(sql5)
    h="<script>window.location='/purchasechild?pid=%s';</script>"%(pmid)
    return HttpResponse(h)
	
def viewpurchasechild(request):
	cur=connection.cursor()
	s="select * from purchasechild"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'pcid':row[0],'pid':row[1],'icode':row[2],'qty':row[3],'amt':row[4],'tamt':row[5]}
		list.append(w)
	return render(request,'viewpurchasechild.html',{'list':list})
	
def delpchild(request):
    cursor=connection.cursor()
    id=request.GET['id']
    sql2="select tamt,pid,qty,icode from purchasechild where pcid='%s'"%(id)
    cursor.execute(sql2)
    result=cursor.fetchall()
    for row in result:
        ctamt=row[0]
        pmid=row[1]
        tqty=int(row[2])
        bid=row[3]
    sql3="select tamt from purchasemaster where pid='%s'"%(pmid)
    cursor.execute(sql3)
    result1=cursor.fetchall()
    for row1 in result1:
        ptamt=row1[0]
    amt=int(ptamt)-int(ctamt)
    sql3="update purchasemaster set tamt='%s'  where pid='%s'"%(amt,pmid)
    cursor.execute(sql3)
    sql="delete from purchasechild where pcid='%s'"%(id)
    cursor.execute(sql)
    sql4="select qty from item where icode='%s'"%(bid)
    cursor.execute(sql4)
    result3=cursor.fetchall()
    for row3 in result3:
        bqty1=int(row3[0])
    bqty=bqty1-tqty
    sql5="update item set qty='%s'  where icode='%s'"%(bqty,bid)
    cursor.execute(sql5)
    h="<script>window.location='/purchasechild?pid=%s';</script>"%(pmid)
    return HttpResponse(h)
	
	
	
	
def porder(request):
	list=porder1(request)
	list1=vstaff1(request)
	return render(request,'porder.html', {'order': list,'staff':list1}) 
	
def assign(request):
	cursor = connection.cursor()
	oid=request.GET['oid'];
	st=request.GET['st'];
	sql="insert into tbl_assign(oid,stid)values('%s','%s')"%(oid,st)
	cursor.execute(sql)
	sql1="update tbl_order set ostatus='Assigned' WHERE oid='%s'"%(oid)
	cursor.execute(sql1)
	h="<script> alert('STAFF ASSIGNED'); window.location='/adminhome/'; </script>"
	return HttpResponse(h)




def orderreport(request):
	cursor = connection.cursor()
	a=request.session['uid']
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select tbl_order.odate,tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal,customer.ctname,customer.phno,customer.chname,customer.city,customer.dist,customer.pin,staff.stfname,customer.cid,item.icode from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode inner join customer on customer.cid=tbl_order.uid inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join staff  on staff.stfid=tbl_assign.stid where tbl_order.odate between '%s' and '%s'   order by tbl_order.oid desc"%(d1,d2) 
	elif (request.method == 'GET' and 'dev' in request.GET):
		sql2="select tbl_order.odate,tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal,customer.ctname,customer.phno,customer.chname,customer.city,customer.dist,customer.pin,staff.stfname,customer.cid,item.icode  from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode inner join customer on customer.cid=tbl_order.uid inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join staff  on staff.stfid=tbl_assign.stid where tbl_order.ostatus='Delivered'   order by tbl_order.oid desc" 
	else:
		sql2="select tbl_order.odate,tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal,customer.ctname,customer.phno,customer.chname,customer.city,customer.dist,customer.pin,staff.stfname,customer.cid,item.icode  from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode inner join customer on customer.cid=tbl_order.uid inner join tbl_assign on tbl_assign.oid=tbl_order.oid		 inner join staff  on staff.stfid=tbl_assign.stid order by tbl_order.oid desc" 
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w= {'odate' : row[0],'ostatus' : row[1],'iname': row[2],'qty' : row[3],'rate': row[4],'p_image' : row[5],'wght':row[6],'mcharge':row[7],'sprice':row[8],'mprice':row[9],'total':row[10],'gtotal':row[11],'cname' : row[12],'cphno': row[13],'chouse' : row[14],'ccity':row[15],'cdist' : row[16],'cpin':row[17],'stfname':row[18],'cid':row[19],'icode':row[20]}
		list.append(w) 
	if (request.method == 'GET' and 'dev' in request.GET):
		return render(request,'dreports.html', {'order': list})
	else:
		return render(request,'reports.html', {'order': list})

def staffreport(request):
	list1=vstaff(request)
	return render(request,'staffreport.html', {'list':list1})    			

def venreport(request):
	list1=vvendor(request)
	return render(request,'venreport.html', {'list':list1})

def purreport(request):
	cursor = connection.cursor()
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select purchasechild.icode,purchasechild.qty,purchasechild.amt,purchasechild.tamt,purchasemaster.dop,purchasemaster.vid from purchasechild  inner join purchasemaster   on purchasemaster.pid=purchasechild.pid  where purchasemaster.dop between '%s' and '%s'"%(d1,d2)
	else:
		sql2="select purchasechild.icode,purchasechild.qty,purchasechild.amt,purchasechild.tamt,purchasemaster.dop,purchasemaster.vid from purchasechild  inner join purchasemaster   on purchasemaster.pid=purchasechild.pid  "
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		price=int(row[1])
		cqty=int(row[3])
		ttt=(cqty*price)
		w = {'icode' : row[0],'pqty': row[1],'pamt' : row[2],'tamt': row[3],'pdate':row[4],'vid':row[5]}
		list.append(w)
	return render(request,'purreports.html', {'list':list})		
	
	
	
	
def logout(request):
	try:
		del request.session['uid']
		del request.session['utype']
	except:
		pass
	return HttpResponse("<script>alert('YOU ARE LOGGED OUT');window.location='/login/';</script>")
	
	
	
	
def vcat(request):
	cur=connection.cursor()
	s="select * from category"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'cname':row[0],'descp':row[1]}
		list.append(w)
	return list
	
def vscat(request):
	cur=connection.cursor()
	s="select * from subcategory"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'scatid':row[0],'scname':row[1],'descp':row[2]}
		list.append(w)
	return list
	
def vrate(s):
	cur=connection.cursor()
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'rid':row[0],'cname':row[1],'rdate':row[2],'rate':row[3]}
		list.append(w)
	return list
	
def vitem(request):
	cur=connection.cursor()
	s="select * from item"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'icode':row[0],'iname':row[1],'cname':row[2],'scname':row[3],'modal':row[4],'wght':row[5],'stonedtl':row[6],'swght':row[7],'sprice':row[8],'mcharge':row[9],'size':row[10],'descp':row[11],'p_image':row[12],'qty':row[13]}
		list.append(w)
	return list

def vstaff(request):
	cur=connection.cursor()
	s="select * from staff"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'stfid':row[0],'stfname':row[1],'shname':row[2],'street':row[3],'city':row[4],'dist':row[5],'pin':row[6],'state':row[7],'phno':row[8],'eml':row[9],'status':row[10]}
		list.append(w)
	return list
	
def vvendor(request):
	cur=connection.cursor()
	s="select * from vendor"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'vid':row[0],'vname':row[1],'oname':row[2],'adrs':row[3],'city':row[4],'dist':row[5],'state':row[6],'pin':row[7],'eml':row[8],'phno':row[9]}
		list.append(w)	
	return list

def vstaff1(request):
	cur=connection.cursor()
	s="select * from staff where status='Active'"
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		w={'stfid':row[0],'stfname':row[1],'shname':row[2],'street':row[3],'city':row[4],'dist':row[5],'pin':row[6],'state':row[7],'phno':row[8],'eml':row[9],'status':row[10]}
		list.append(w)
	return list

def vproduct(request):
    cursor = connection.cursor()
    if (request.method == 'GET' and 'srh' in request.GET):
        se=request.GET['srh']
        p="select item.*  from item  inner join category on item.cname=category.cname inner join subcategory on item.scname=subcategory.scname   where item.icode like '%%%s%%' or  item.iname like '%%%s%%' or  category.cname like '%%%s%%' or  subcategory.scname like '%%%s%%' " %(se,se,se,se)
    else:
        p="select item.*  from item  inner join category on item.cname=category.cname inner join subcategory on item.scname=subcategory.scname "
    cursor.execute(p)
    re1=cursor.fetchall()
    pdt=[]
    for row in re1:
		w={'icode':row[0],'iname':row[1],'cname':row[2],'scname':row[3],'modal':row[4],'wght':row[5],'stonedtl':row[6],'swght':row[7],'sprice':row[8],'mcharge':row[9],'size':row[10],'descp':row[11],'p_image':row[12],'qty':row[13]}
		pdt.append(w)
    return render(request,'vproducts.html', {'list':pdt})

def pdetails(request):
	cur=connection.cursor()
	cursor=connection.cursor()
	s="select * from item where icode='%s'"%(request.GET['id'])
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		wght=row[5]
		mc=row[9]
		sp=row[8]
		cname=row[2]
		w={'icode':row[0],'iname':row[1],'cname':row[2],'scname':row[3],'modal':row[4],'wght':row[5],'stonedtl':row[6],'swght':row[7],'sprice':row[8],'mcharge':row[9],'size':row[10],'descp':row[11],'p_image':row[12],'qty':row[13]}
		list.append(w)
	sq="select rate from rate where  rid=(select max(rid) from rate where rdate='%s' and cname='%s')"%(today,cname)
	cursor.execute(sq)
	#return HttpResponse(sq)
	if(cursor.rowcount>0):
		#return HttpResponse(sq)
		result=cursor.fetchall()
		for row in result:
			rate=row[0]
	else:
		sq2="select rate from rate where  rid=(select max(rid) from rate where cname='%s')"%(cname)
		cur.execute(sq2)
		result2=cur.fetchall()
		for row2 in result2:
			rate=row2[0]
	#return HttpResponse(rate)
	tot=float(rate)*float(wght)
	m=(tot*float(mc))/100.0
	gt=tot+m+int(sp)
	return render(request,'pdetails.html',{'list':list,'rate':rate,'tot':tot,'gtotal':gt})
	
def cart(request):
    cursor=connection.cursor()
    bi=request.GET['bi']
    qty=request.GET['qty']
    uid=request.session['uid']
    sql2="select * from cart where icode='%s' and cid='%s'"%(bi,uid)
    cursor.execute(sql2)
    result=cursor.fetchall()
    if(cursor.rowcount>0):
        h="<script>alert('ITEM ALREADY EXISTS IN CART');window.location='/custhome/';</script>"
    else:  
        sql1="insert into cart(icode,cid,cqty) values('%s','%s','%s')" %(bi,uid,qty)
        cursor.execute(sql1)
        h="<script>window.location='/vcart/';</script>"
    return HttpResponse(h)
	
def vcart(request):
	cursor = connection.cursor()
	cur = connection.cursor()
	uid=request.session['uid']
	p="select item.icode,item.cname,item.iname,item.wght,item.mcharge,item.sprice,item.p_image,cart.cqty,cart.cartid,item.qty from item INNER JOIN cart ON cart.icode=item.icode where cart.cid='%s'" %(uid)
	cur.execute(p)
	#return HttpResponse(p)
	re1=cur.fetchall()
	pdt=[]
	gtotal=0
	total=0
	rate=0
	if cur.rowcount>0:
		for sy3 in re1:
			sq="select rate from rate where  rid=(select max(rid) from rate where rdate='%s' and cname='%s')"%(today,sy3[1])
			cursor.execute(sq)
			if(cursor.rowcount>0):
				result=cursor.fetchall()
				for row in result:
					rate=float(row[0])
			else:
				sq2="select rate from rate where  rid=(select max(rid) from  rate where cname='%s')"%(sy3[1])
				cur.execute(sq2)
				result2=cur.fetchall()
				for row2 in result2:
					rate=float(row2[0])	
			cqty=float(sy3[7])
			tot=float(rate)*float(sy3[3])
			m=(tot*float(sy3[4]))/100.0
			sp=float(sy3[5])
			gt=(tot+m+float(sp))
			total=(gt*int(sy3[7]))
			gtotal=(gtotal+total)
			y3 = {'icode':sy3[0],'iname' : sy3[2],'wght' : sy3[3],'mcharge' : sy3[4],'sprice' : sy3[5],'p_image':sy3[6],'cqty' : sy3[7],'cartid':sy3[8],'qty':sy3[9],'rate':rate,'mrate':m,'gt':gt,'tot':tot,'total':total}
			pdt.append(y3)
	return render(request,'vcart.html', {'list':pdt,'gtotal':gtotal,'date':today})
	
def delcart(request):
    cursor=connection.cursor()
    id=request.GET['id']
    sql="delete from cart where cartid='%s'"%(id)
    cursor.execute(sql)
    h="<script>window.location='/vcart/';</script>"
    return HttpResponse(h)

def buyaction(request):
    cursor=connection.cursor()
    cur=connection.cursor()
    cursor1=connection.cursor()
    uid=request.session['uid'];
    cardno=request.GET['vnm'];
    cvv=request.GET['bnm'];
    edate=request.GET['edate'];
    tamount=request.GET['stnm'];
    odate=today
    s1="select sum(cqty) as cnt from cart where cid='%s'"%(uid)
    cursor.execute(s1)
    result=cursor.fetchall()
    tamt=0
    for row in result:
        tqty=row[0]
    #--------------------------------------------------
    sql="insert into tbl_order(uid,tqty,tamt,ostatus,odate) values ('%s','%s','%s','%s','%s')"%(uid,tqty,'0','pending',odate)
    cursor.execute(sql)
    #-------------------------------------
    ss="select max(oid) as oid from tbl_order"
    cursor.execute(ss)
    result1=cursor.fetchall()
    for c1 in result1:
        oid=c1[0]
    #---------------------------------------------------
	gtotal=0
	total=0
	rate=0	
    s="select * from cart where cid=%s"%(uid)
    cursor.execute(s)
    result2=cursor.fetchall()
    for r1 in result2:
		p="select item.icode,item.cname,item.iname,item.wght,item.mcharge,item.sprice,item.p_image,cart.cqty,cart.cartid,item.qty from item INNER JOIN cart ON cart.icode=item.icode where  item.icode='%s'" %(r1[2])
		cur.execute(p)
		#return HttpResponse(p)
		re1=cur.fetchall()
		pdt=[]
		if cur.rowcount>0:
			for sy3 in re1:
				sq="select rate from rate where  rid=(select max(rid) from rate where rdate='%s' and cname='%s')"%(today,sy3[1])
				cursor1.execute(sq)
				#return HttpResponse(cursor1.rowcount)
				if(cursor1.rowcount>0):
					result=cursor1.fetchall()
					for row in result:
						rate1=float(row[0])
				else:
					sq2="select rate from rate where  rid=(select max(rid) from  rate where cname='%s')"%(sy3[1])
					cur.execute(sq2)
					result2=cur.fetchall()
					for row2 in result2:
						rate1=float(row2[0])	
				cqty=float(sy3[7])
				tot=float(rate1)*float(sy3[3])
				m=(tot*float(sy3[4]))/100.0
				sp=float(sy3[5])
				gt=(tot+m+float(sp))
				total=(gt*int(sy3[7]))
				gtotal=(gtotal+total)

                pqty=int(sy3[9])
                ssss=int(sy3[7])
                stqty=pqty-ssss
		sql1="insert into tbl_orderc(oid,icode,qty,rate,wght,mcharge,sprice,mprice,total,gtotal) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(oid,sy3[0],cqty,rate1,sy3[3],m,sp,tot,gt,total)
		cursor.execute(sql1)
		#return HttpResponse(sql1)
		sqle="update item set qty='%s' where icode='%s'" %(stqty,sy3[0])
		cursor.execute(sqle)
		sql2="delete from cart where cid='%s' and icode='%s'"%(uid,sy3[0])
		cursor.execute(sql2)
    #------------------------------------------------
    s2="update tbl_order set tamt='%s' where oid='%s'"%(gtotal,oid)
    cursor.execute(s2)
    sql3="insert into tbl_pay(oid,uid,cardno,cvv,edate)values('%s','%s','%s','%s','%s')"%(oid,uid,cardno,cvv,edate)
    cursor.execute(sql3)
    h="<script> alert('SUCCESS'); window.location='/myorder/'; </script>"
    return HttpResponse(h)  
	
def myorder(request):
    cursor = connection.cursor()
    a=request.session['uid']
    sql2="select tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode where tbl_order.uid='%s' order by tbl_order.oid desc"%(a)
    cursor.execute(sql2)
    result=cursor.fetchall()
    list=[]
    total=0
    for row in result:
        cqty=int(row[2])
        #return HttpResponse(cqty)
        price=int(row[3])
        ttt=(cqty*price)
        total=total+ttt
        w = {'ostatus' : row[0],'iname': row[1],'qty' : row[2],'rate': row[3],'p_image' : row[4],'wght':row[5],'mcharge':row[6],'sprice':row[7],'mprice':row[8],'total':row[9],'gtotal':row[10]}
        list.append(w)   
    #list1=vcat(request)
    return render(request,'myorder.html', {'list': list}) 
	
def porder1(request):
	cursor = connection.cursor()
	a=request.session['uid']
	sql2="select tbl_order.oid,tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal,customer.ctname,customer.phno,customer.chname,customer.city,customer.dist,customer.pin,item.icode from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode inner join customer on customer.cid=tbl_order.uid where tbl_order.ostatus='pending' order by tbl_order.oid desc" 
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {'oid' : row[0],'ostatus' : row[1],'iname': row[2],'qty' : row[3],'rate': row[4],'p_image' : row[5],'wght':row[6],'mcharge':row[7],'sprice':row[8],'mprice':row[9],'total':row[10],'gtotal':row[11],'cname' : row[12],'cphno': row[13],'chouse' : row[14],'ccity':row[15],'cdist' : row[16],'cpin':row[17],'icode':row[18]}
		list.append(w)
	return list

def aorders(request):
	cursor = connection.cursor()
	uid=request.session['uid']
	sql2="select tbl_order.odate,tbl_order.ostatus,item.iname,tbl_orderc.qty,tbl_orderc.rate,item.p_image,tbl_orderc.wght,tbl_orderc.mcharge,tbl_orderc.sprice,tbl_orderc.mprice,tbl_orderc.total,tbl_orderc.gtotal,customer.ctname,customer.phno,customer.chname,customer.city,customer.dist,customer.pin,tbl_order.oid  from tbl_order inner join tbl_orderc on tbl_orderc.oid=tbl_order.oid inner join item on item.icode=tbl_orderc.icode inner join customer on customer.cid=tbl_order.uid inner join tbl_assign on tbl_assign.oid=tbl_order.oid where tbl_assign.stid='%s' order by tbl_order.oid desc"%(uid)	
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w= {'odate' : row[0],'ostatus' : row[1],'iname': row[2],'qty' : row[3],'rate': row[4],'p_image' : row[5],'wght':row[6],'mcharge':row[7],'sprice':row[8],'mprice':row[9],'total':row[10],'gtotal':row[11],'cname' : row[12],'cphno': row[13],'chouse' : row[14],'ccity':row[15],'cdist' : row[16],'cpin':row[17],'oid':row[18]}
		list.append(w) 
	return render(request,'aorders.html', {'order': list})
	
def status(request):
	cursor = connection.cursor()
	oid=request.GET['oid']
	sts=request.GET['s']
	sql="update tbl_order set ostatus='%s' WHERE oid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>  window.location='/aorders/'; </script>"
	return HttpResponse(h)
	
def upcart(request):
	cur=connection.cursor()
	cursor=connection.cursor()
	s="select cartid from  cart where cid='%s'"%(request.session['uid'])
	cur.execute(s)
	list=[]
	result=cur.fetchall()
	for row in result:
		q=int(request.GET['t1'+str(row[0])])
		sql="update cart set cqty='%s' WHERE cartid='%s'"%(q,row[0])
		cursor.execute(sql)
	uid=request.session['uid']
	p="select item.icode,item.cname,item.iname,item.wght,item.mcharge,item.sprice,item.p_image,cart.cqty,cart.cartid from item INNER JOIN cart ON cart.icode=item.icode where cart.cid='%s'" %(uid)
	cur.execute(p)
	#return HttpResponse(p)
	re1=cur.fetchall()
	pdt=[]
	gtotal=0
	total=0
	rate=0
	if cur.rowcount>0:
		for sy3 in re1:
			sq="select rate from rate where  rid=(select max(rid) from rate where rdate='%s' and cname='%s')"%(today,sy3[1])
			cursor.execute(sq)
			if(cursor.rowcount>0):
				result=cursor.fetchall()
				for row in result:
					rate=float(row[0])
			else:
				sq2="select rate from rate where  rid=(select max(rid) from  rate where cname='%s')"%(sy3[1])
				cur.execute(sq2)
				result2=cur.fetchall()
				for row2 in result2:
					rate=float(row2[0])	
			cqty=float(sy3[7])
			tot=float(rate)*float(sy3[3])
			m=(tot*float(sy3[4]))/100.0
			sp=float(sy3[5])
			gt=(tot+m+float(sp))
			total=(gt*int(sy3[7]))
			gtotal=(gtotal+total)
			y3 = {'icode':sy3[0],'iname' : sy3[2],'wght' : sy3[3],'mcharge' : sy3[4],'sprice' : sy3[5],'p_image':sy3[6],'cqty' : sy3[7],'cartid':sy3[8],'rate':rate,'mrate':m,'gt':gt,'tot':tot,'total':total}
			pdt.append(y3)
	return render(request,'vcart1.html', {'list':pdt,'gtotal':gtotal,'date':today})

def salereport(request):
	cursor = connection.cursor()
	a=request.session['uid']
	if (request.method == 'GET' and 'd1' in request.GET)and (request.method == 'GET' and 'd2' in request.GET):
		d1=request.GET['d1']
		d2=request.GET['d2']
		sql2="select tbl_item.itname,tbl_orderchild.qty,tbl_orderm.odate,tbl_item.mrp,tbl_item.p_image,tbl_orderm.ostatus,tbl_staff.sfname,tbl_customer.cfname,tbl_customer.phno,tbl_customer.phno from tbl_orderm inner join tbl_orderchild on tbl_orderchild.oid=tbl_orderm.oid inner join tbl_item on tbl_item.icode=tbl_orderchild.icode inner join tbl_customer   on tbl_customer.custid=tbl_orderm.custid  inner join tbl_assign on tbl_assign.oid=tbl_orderm.oid		 inner join tbl_staff  on tbl_staff.sid=tbl_assign.stid where odate between '%s' and '%s'   order by tbl_orderm.oid desc"%(d1,d2)
	else:
		sql2="select tbl_item.itname,tbl_orderchild.qty,tbl_orderm.odate,tbl_item.mrp,tbl_item.p_image,tbl_orderm.ostatus,tbl_staff.sfname,tbl_customer.cfname,tbl_customer.phno,tbl_customer.email from tbl_orderm inner join tbl_orderchild on tbl_orderchild.oid=tbl_orderm.oid inner join tbl_item on tbl_item.icode=tbl_orderchild.icode inner join tbl_customer   on tbl_customer.custid=tbl_orderm.custid  inner join tbl_assign on tbl_assign.oid=tbl_orderm.oid		 inner join tbl_staff  on tbl_staff.sid=tbl_assign.stid  order by tbl_orderm.oid desc"
	
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		price=int(row[1])
		cqty=int(row[3])
		ttt=(cqty*price)
		w = {'book_name' : row[0],'qty': row[1],'odate' : row[2],'book_price': row[3],'book_image' : row[4],'ostatus' : row[5],'staff_name': row[6],'cname' : row[7],'cpho': row[8],'cemail':row[9],'total':ttt}#,'cdist' : row[10],'cpin':row[11]}
		list.append(w)
	return render(request,'salereports.html', {'list':list})