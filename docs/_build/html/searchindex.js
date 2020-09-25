Search.setIndex({docnames:["accounts","accounts.migrations","core","core.migrations","core.templatetags","developer","developer.migrations","index","manage","mega_backend","modules"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["accounts.rst","accounts.migrations.rst","core.rst","core.migrations.rst","core.templatetags.rst","developer.rst","developer.migrations.rst","index.rst","manage.rst","mega_backend.rst","modules.rst"],objects:{"":{accounts:[0,0,0,"-"],core:[2,0,0,"-"],developer:[5,0,0,"-"],manage:[8,0,0,"-"],mega_backend:[9,0,0,"-"]},"accounts.apps":{AccountsConfig:[0,1,1,""]},"accounts.apps.AccountsConfig":{name:[0,2,1,""],ready:[0,3,1,""]},"accounts.forms":{MyAuthenticationForm:[0,1,1,""],MySetPasswordForm:[0,1,1,""]},"accounts.forms.MyAuthenticationForm":{base_fields:[0,2,1,""],declared_fields:[0,2,1,""],media:[0,3,1,""]},"accounts.forms.MySetPasswordForm":{base_fields:[0,2,1,""],declared_fields:[0,2,1,""],media:[0,3,1,""]},"accounts.migrations":{"0001_initial":[1,0,0,"-"]},"accounts.migrations.0001_initial":{Migration:[1,1,1,""]},"accounts.migrations.0001_initial.Migration":{dependencies:[1,2,1,""],initial:[1,2,1,""],operations:[1,2,1,""]},"accounts.models":{Profile:[0,1,1,""]},"accounts.models.Profile":{DoesNotExist:[0,4,1,""],MultipleObjectsReturned:[0,4,1,""],id:[0,2,1,""],objects:[0,2,1,""],phone_number:[0,2,1,"id0"],picture:[0,2,1,"id1"],user:[0,2,1,"id2"],user_id:[0,2,1,""]},"accounts.serializers":{ProfileSerializer:[0,1,1,""],SpecialUserSerializer:[0,1,1,""]},"accounts.serializers.ProfileSerializer":{Meta:[0,1,1,""]},"accounts.serializers.ProfileSerializer.Meta":{fields:[0,2,1,""],model:[0,2,1,""],read_only_fields:[0,2,1,""]},"accounts.serializers.SpecialUserSerializer":{Meta:[0,1,1,""]},"accounts.serializers.SpecialUserSerializer.Meta":{exclude:[0,2,1,""],model:[0,2,1,""],read_only_fields:[0,2,1,""]},"accounts.signals":{create_profile:[0,5,1,""],save_user_profile:[0,5,1,""],save_username:[0,5,1,""]},"accounts.tests":{ProfileViewTest:[0,1,1,""],SignalsTest:[0,1,1,""]},"accounts.tests.ProfileViewTest":{setUp:[0,3,1,""],test_profile_queryset_correct:[0,3,1,""]},"accounts.tests.SignalsTest":{setUp:[0,3,1,""],test_profile_created:[0,3,1,""],test_username_is_assigned_when_user_created:[0,3,1,""]},"accounts.views":{ProfileViewSet:[0,1,1,""],SpecialUserView:[0,1,1,""]},"accounts.views.ProfileViewSet":{get_queryset:[0,3,1,""],parser_classes:[0,2,1,""],permission_classes:[0,2,1,""],serializer_class:[0,2,1,""]},"accounts.views.SpecialUserView":{get:[0,3,1,""],patch:[0,3,1,""]},"core.apps":{CoreConfig:[2,1,1,""]},"core.apps.CoreConfig":{name:[2,2,1,""]},"core.migrations":{"0001_initial":[3,0,0,"-"]},"core.migrations.0001_initial":{Migration:[3,1,1,""]},"core.migrations.0001_initial.Migration":{dependencies:[3,2,1,""],initial:[3,2,1,""],operations:[3,2,1,""]},"core.models":{Community:[2,1,1,""],CommunityType:[2,1,1,""],DataAccessType:[2,1,1,""],Feature:[2,1,1,""],SimpleStore:[2,1,1,""],UploadedImage:[2,1,1,""],get_random_key:[2,5,1,""]},"core.models.Community":{DoesNotExist:[2,4,1,""],MultipleObjectsReturned:[2,4,1,""],admins:[2,2,1,"id0"],description:[2,2,1,"id1"],features:[2,2,1,"id2"],get_community_type_value:[2,3,1,""],id:[2,2,1,""],is_admin:[2,3,1,""],is_admin_or_member:[2,3,1,""],key:[2,2,1,"id3"],members:[2,2,1,"id4"],name:[2,2,1,"id5"],objects:[2,2,1,""],picture:[2,2,1,"id6"],save:[2,3,1,""],simple_store:[2,2,1,""],type:[2,2,1,"id7"],type_id:[2,2,1,""]},"core.models.CommunityType":{DoesNotExist:[2,4,1,""],MultipleObjectsReturned:[2,4,1,""],communities_with_type:[2,2,1,""],id:[2,2,1,""],objects:[2,2,1,""],value:[2,2,1,"id8"]},"core.models.DataAccessType":{ADMIN:[2,2,1,"id9"],COMMUNITY:[2,2,1,"id10"],USER:[2,2,1,"id11"]},"core.models.Feature":{DoesNotExist:[2,4,1,""],MultipleObjectsReturned:[2,4,1,""],User:[2,2,1,""],approved:[2,2,1,"id12"],communities_using:[2,2,1,""],description:[2,2,1,""],desription:[2,2,1,""],id:[2,2,1,""],key:[2,2,1,"id13"],name:[2,2,1,"id14"],objects:[2,2,1,""],payload:[2,2,1,"id15"],picture:[2,2,1,"id16"],save:[2,3,1,""],simple_store:[2,2,1,""],user:[2,2,1,""],user_id:[2,2,1,""]},"core.models.SimpleStore":{DoesNotExist:[2,4,1,""],MultipleObjectsReturned:[2,4,1,""],access:[2,2,1,"id17"],community:[2,2,1,"id18"],community_id:[2,2,1,""],date:[2,2,1,"id19"],feature:[2,2,1,"id20"],feature_id:[2,2,1,""],get_access_display:[2,3,1,""],get_next_by_date:[2,3,1,""],get_previous_by_date:[2,3,1,""],id:[2,2,1,""],key:[2,2,1,"id21"],objects:[2,2,1,""],user:[2,2,1,"id22"],user_id:[2,2,1,""],value:[2,2,1,"id23"]},"core.models.UploadedImage":{DoesNotExist:[2,4,1,""],MultipleObjectsReturned:[2,4,1,""],id:[2,2,1,""],image:[2,2,1,"id24"],objects:[2,2,1,""]},"core.permissions":{IsCommunityAdmin:[2,1,1,""],IsOwner:[2,1,1,""]},"core.permissions.IsCommunityAdmin":{has_object_permission:[2,3,1,""]},"core.permissions.IsOwner":{has_object_permission:[2,3,1,""]},"core.serializers":{CommunitySerializer:[2,1,1,""],CommunityTypeSerializer:[2,1,1,""],FeatureSerializer:[2,1,1,""],SimpleStoreSerializer:[2,1,1,""]},"core.serializers.CommunitySerializer":{Meta:[2,1,1,""]},"core.serializers.CommunitySerializer.Meta":{exclude:[2,2,1,""],model:[2,2,1,""],read_only_fields:[2,2,1,""]},"core.serializers.CommunityTypeSerializer":{Meta:[2,1,1,""]},"core.serializers.CommunityTypeSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""],read_only_fields:[2,2,1,""]},"core.serializers.FeatureSerializer":{Meta:[2,1,1,""]},"core.serializers.FeatureSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""],read_only_fields:[2,2,1,""]},"core.serializers.SimpleStoreSerializer":{Meta:[2,1,1,""]},"core.serializers.SimpleStoreSerializer.Meta":{fields:[2,2,1,""],model:[2,2,1,""],read_only_fields:[2,2,1,""]},"core.tests":{AddFeatureToCommunityTestCase:[2,1,1,""],CheckEmailViewTestCase:[2,1,1,""],CommunityModelTestCase:[2,1,1,""],CommunityViewTestCase:[2,1,1,""],DataStoreTestCase:[2,1,1,""],FeatureModelTestCase:[2,1,1,""],FeatureViewTestCase:[2,1,1,""],JoinCommunityTestCase:[2,1,1,""],LeaveCommunityTestCase:[2,1,1,""],RemoveFeatureTestCase:[2,1,1,""]},"core.tests.AddFeatureToCommunityTestCase":{setUp:[2,3,1,""],test_add_feature:[2,3,1,""],test_add_feature_errors:[2,3,1,""]},"core.tests.CheckEmailViewTestCase":{setUp:[2,3,1,""],test_check_email:[2,3,1,""]},"core.tests.CommunityModelTestCase":{setUp:[2,3,1,""],test_community_key_is_unique:[2,3,1,""],test_get_community_type_value:[2,3,1,""],test_is_admin:[2,3,1,""],test_is_admin_or_member:[2,3,1,""]},"core.tests.CommunityViewTestCase":{setUp:[2,3,1,""],test_community_perform_create:[2,3,1,""],test_community_queryset_is_accurate:[2,3,1,""]},"core.tests.FeatureModelTestCase":{setUp:[2,3,1,""],test_feature_key_is_unique:[2,3,1,""]},"core.tests.FeatureViewTestCase":{setUp:[2,3,1,""],test_feature_queryset_is_accurate:[2,3,1,""]},"core.tests.JoinCommunityTestCase":{setUp:[2,3,1,""],test_join_community:[2,3,1,""],test_join_community_errors:[2,3,1,""]},"core.tests.LeaveCommunityTestCase":{setUp:[2,3,1,""],test_leave_community:[2,3,1,""],test_leave_community_errors:[2,3,1,""]},"core.tests.RemoveFeatureTestCase":{setUp:[2,3,1,""],test_remove_feature:[2,3,1,""],test_remove_feature_errors:[2,3,1,""]},"core.views":{AddFeatureToCommunity:[2,1,1,""],CheckEmail:[2,1,1,""],CommunityTypeViewSet:[2,1,1,""],CommunityViewSet:[2,1,1,""],DataStore:[2,1,1,""],DataStoreDetails:[2,1,1,""],FeatureViewSet:[2,1,1,""],JoinCommunity:[2,1,1,""],LeaveCommunity:[2,1,1,""],RemoveFeature:[2,1,1,""],UploadImage:[2,1,1,""],filter_stores_by_access:[2,5,1,""]},"core.views.AddFeatureToCommunity":{post:[2,3,1,""]},"core.views.CheckEmail":{post:[2,3,1,""]},"core.views.CommunityTypeViewSet":{queryset:[2,2,1,""],serializer_class:[2,2,1,""]},"core.views.CommunityViewSet":{get_queryset:[2,3,1,""],parser_classes:[2,2,1,""],perform_create:[2,3,1,""],permission_classes:[2,2,1,""],serializer_class:[2,2,1,""]},"core.views.DataStore":{get:[2,3,1,""],post:[2,3,1,""]},"core.views.DataStoreDetails":{"delete":[2,3,1,""]},"core.views.FeatureViewSet":{get_queryset:[2,3,1,""],serializer_class:[2,2,1,""]},"core.views.JoinCommunity":{post:[2,3,1,""]},"core.views.LeaveCommunity":{post:[2,3,1,""]},"core.views.RemoveFeature":{post:[2,3,1,""]},"core.views.UploadImage":{parser_class:[2,2,1,""],post:[2,3,1,""]},"developer.apps":{DeveloperConfig:[5,1,1,""]},"developer.apps.DeveloperConfig":{name:[5,2,1,""]},"developer.forms":{FeatureForm:[5,1,1,""]},"developer.forms.FeatureForm":{Meta:[5,1,1,""],base_fields:[5,2,1,""],declared_fields:[5,2,1,""],media:[5,3,1,""]},"developer.forms.FeatureForm.Meta":{fields:[5,2,1,""],labels:[5,2,1,""],model:[5,2,1,""]},"developer.tests":{DeveloperWebTest:[5,1,1,""]},"developer.tests.DeveloperWebTest":{setUp:[5,3,1,""],test_accurate_feature_details_are_displayed:[5,3,1,""],test_accurate_features_are_displayed:[5,3,1,""],test_add_feature_page_loads:[5,3,1,""],test_edit_feature_page_loads:[5,3,1,""],test_feature_detail_page_loads:[5,3,1,""],test_feature_is_created:[5,3,1,""],test_feature_is_edited:[5,3,1,""],test_index_page_loads:[5,3,1,""]},"developer.views":{add_feature:[5,5,1,""],delete_feature:[5,5,1,""],edit_feature:[5,5,1,""],feature_details:[5,5,1,""],index:[5,5,1,""]},accounts:{admin:[0,0,0,"-"],apps:[0,0,0,"-"],forms:[0,0,0,"-"],migrations:[1,0,0,"-"],models:[0,0,0,"-"],serializers:[0,0,0,"-"],signals:[0,0,0,"-"],tests:[0,0,0,"-"],urls:[0,0,0,"-"],views:[0,0,0,"-"]},core:{admin:[2,0,0,"-"],apps:[2,0,0,"-"],migrations:[3,0,0,"-"],models:[2,0,0,"-"],permissions:[2,0,0,"-"],serializers:[2,0,0,"-"],templatetags:[4,0,0,"-"],tests:[2,0,0,"-"],urls:[2,0,0,"-"],views:[2,0,0,"-"]},developer:{admin:[5,0,0,"-"],apps:[5,0,0,"-"],forms:[5,0,0,"-"],migrations:[6,0,0,"-"],models:[5,0,0,"-"],tests:[5,0,0,"-"],urls:[5,0,0,"-"],views:[5,0,0,"-"]},manage:{main:[8,5,1,""]},mega_backend:{asgi:[9,0,0,"-"],settings:[9,0,0,"-"],urls:[9,0,0,"-"],wsgi:[9,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","method","Python method"],"4":["py","exception","Python exception"],"5":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:method","4":"py:exception","5":"py:function"},terms:{"0001_initi":[0,2,10],"3rd":2,"class":[0,1,2,3,5],"default":[0,2],"enum":2,"function":2,"int":5,"return":[0,2,5],"true":[1,2,3],For:9,The:[0,2,5,9],These:2,UIs:2,__all__:[0,2],__first__:[1,3],accept:2,access:[2,3],accessor:[0,2],account:10,accountsconfig:0,accur:2,add:[2,5],add_featur:5,added:2,addfeaturetocommun:2,addfeaturetocommunitytestcas:2,addfield:3,adding:2,admin:[3,9,10],administr:8,admn:2,alia:[0,2,5],all:[0,2,5],allow:2,alwai:2,api:2,apiview:[0,2],app:10,app_label:[1,3],app_modul:[0,2,5],app_nam:[0,2,5],appconfig:[0,2,5],applic:9,appropri:[0,2],approv:[2,3],arg:[0,2,5],asgi:10,assign:[0,2],associ:[0,2],attribut:2,auth:[0,1,2,3],authent:0,authenticationform:0,autofield:[1,3],avail:2,backend:[0,2,5],base:[0,1,2,3,5],base_field:[0,5],basepermiss:2,becaus:2,been:2,befor:[0,2,5],being:2,below:2,bool:2,built:2,cach:2,callabl:9,can:2,charact:2,charfield:[0,1,2,3,5],check:[0,2],checkemail:2,checkemailviewtestcas:2,child:2,children:2,code:[0,2,5],com:9,command:8,comment:2,commun:[2,3],communities_us:2,communities_with_typ:2,community_id:2,communitymodeltestcas:2,communityseri:2,communitytyp:[2,3],communitytypeseri:2,communitytypeviewset:2,communityviewset:2,communityviewtestcas:2,complex:2,compon:2,config:[0,2,5,9],configur:9,consol:2,contain:[0,2,5],content:10,contrib:[0,2,3],control:2,core:[0,5,10],coreconfig:2,correct:[2,5],creat:[0,2,5],create_forward_many_to_many_manag:2,create_profil:0,createmodel:[1,3],crud:2,current:[0,2],custom:[0,2],data:[0,2],dataaccesstyp:2,databas:2,datastor:2,datastoredelet:[],datastoredetail:2,datastoretestcas:2,date:[2,3],datetimefield:[2,3],declared_field:[0,5],defer:[0,2],defin:2,deleg:2,delet:[2,5],delete_featur:5,depend:[1,2,3],deploy:9,descript:[2,3,5],desript:2,detail:[2,5],detect:2,determin:[2,5],develop:[2,10],developerconfig:5,developerwebtest:5,differ:[0,2],directli:2,displai:[2,5],django:[0,1,2,3,5,8,9],djangoproject:9,doc:9,doesnotexist:[0,2],due:2,dynam:2,edit:[2,5],edit_featur:5,email:2,enumer:2,equival:2,error:2,estat:[],evalu:2,everi:[0,2],exampl:[0,2],except:[0,2],exclud:[0,2],execut:[0,2],exercis:[0,2,5],exist:2,expos:9,extra:0,fals:2,featur:[2,3,5],feature_detail:5,feature_id:[2,5],featureform:5,featuremodeltestcas:2,featureseri:2,featureviewset:2,featureviewtestcas:2,field:[0,1,2,3,5],file:[1,3,9],filedescriptor:[0,2],filter_stores_by_access:2,fire:0,first:[0,2],fixtur:[0,2,5],force_insert:2,force_upd:2,foreignkei:[2,3],form:10,forward:[0,2],forwardmanytoonedescriptor:2,forwardonetoonedescriptor:[0,2],free:2,from:[0,2],frontend:2,full:9,gain:2,gener:[2,9],get:[0,2],get_access_displai:2,get_community_type_valu:2,get_next_by_d:2,get_previous_by_d:2,get_queryset:[0,2],get_random_kei:2,given:0,grant:[],has:2,has_object_permiss:2,have:2,height:[0,2],height_field:[0,2],heroku:2,hold:0,home:5,hook:[0,2,5],how:2,howto:9,http:[5,9],human:2,imag:[2,3],imagefield:[0,1,2,3,5],implement:2,incom:2,index:[5,7],inform:9,initi:[1,3],insert:2,insist:2,instanc:[0,2],instruct:2,is_admin:2,is_admin_or_memb:2,is_next:2,iscommunityadmin:2,isown:[0,2],item:2,iter:2,its:2,join:2,joincommun:2,joincommunitytestcas:2,json:2,jsonb:3,jsonfield:3,just:[0,2],kei:[2,3],kwarg:[0,2,5],label:5,last:2,leav:2,leavecommun:2,leavecommunitytestcas:2,level:[2,9],like:[0,2],limit:2,line:8,list:[2,9],load:[0,2,5],logic:[0,2,5],mai:2,main:8,manag:[0,2,10],mani:2,manual:2,manytomanydescriptor:2,manytomanyfield:[2,3],match:[2,5],media:[0,5],member:[2,3],membership:2,meta:[0,2,5],method:[0,2,5],methodnam:[0,2,5],migrat:[0,2,5,10],model:[1,3,10],model_nam:3,modelform:5,modelseri:[0,2],modelviewset:[0,2],modifi:[],modul:[7,10],more:9,most:2,multipartpars:[0,2],multipleobjectsreturn:[0,2],must:2,myauthenticationform:0,mysetpasswordform:0,name:[0,1,2,3,5,9],need:2,neither:2,new_password1:0,new_password2:0,non:2,none:[0,2,5],normal:2,note:2,nullbooleanfield:3,number:0,obj:2,object:[0,2,5],objectdoesnotexist:[0,2],onc:2,one:[0,2],onetoonefield:[0,1],onli:[0,2],oper:[1,2,3],option:3,order:3,organis:2,otherwis:2,overrid:[0,2],own:2,owner:2,packag:10,page:[5,7],paramet:[0,2,5],parent:2,parser:[0,2],parser_class:[0,2],parti:2,password:0,patch:0,payload:[2,3,5],perform:2,perform_cr:2,permiss:[0,10],permission_class:[0,2],phone:0,phone_numb:[0,1],pictur:[0,1,2,3,5],pizza:2,place:0,post:2,postgr:[2,3],process:2,profil:[0,1],profileseri:0,profileviewset:0,profileviewtest:0,project:9,properli:[0,2],properti:[0,5],provid:2,publ:2,queri:[0,2],queryset:[0,2],random:2,rather:2,read:[0,2],read_only_field:[0,2],readabl:2,readi:0,ref:9,regist:[0,2],reject:2,relat:[0,1,2,3,5],related_nam:[0,2],remov:2,removefeatur:2,removefeaturetestcas:2,render:[0,5],repres:2,request:[0,2,5],requir:[0,5],respect:2,respons:[2,5],rest:2,rest_framework:[0,2],restaur:[0,2],result:2,retriev:2,revers:2,reversemanytoonedescriptor:2,rout:9,run:0,runtest:[0,2,5],save:2,save_user_profil:0,save_usernam:0,search:7,secret:2,see:9,self:2,sender:0,sent:2,serial:10,serializer_class:[0,2],server:2,set:[0,2,5,10],setpasswordform:0,setup:[0,2,5],should:2,side:[0,2],signal:10,signalstest:0,signifi:2,simpl:2,simple_stor:2,simplestor:[2,3],simplestoreseri:2,smoothli:2,specialuserseri:0,specialuserview:0,specif:2,specifi:[2,5],sql:2,sqlite:2,start:0,startproject:9,store:2,store_id:2,str:[0,2],string:2,subclass:[0,2],submodul:10,subpackag:10,subsequ:2,system:[0,2,5],task:8,templatetag:[2,10],test:10,test_accurate_feature_details_are_displai:5,test_accurate_features_are_displai:5,test_add_featur:2,test_add_feature_error:2,test_add_feature_page_load:5,test_check_email:2,test_community_key_is_uniqu:2,test_community_perform_cr:2,test_community_queryset_is_accur:2,test_edit_feature_page_load:5,test_feature_detail_page_load:5,test_feature_is_cr:5,test_feature_is_edit:5,test_feature_key_is_uniqu:2,test_feature_queryset_is_accur:2,test_get_community_type_valu:2,test_index_page_load:5,test_is_admin:2,test_is_admin_or_memb:2,test_join_commun:2,test_join_community_error:2,test_leave_commun:2,test_leave_community_error:2,test_profile_cr:0,test_profile_queryset_correct:0,test_remove_featur:2,test_remove_feature_error:2,test_username_is_assigned_when_user_cr:0,testcas:[0,2,5],textchoic:2,textfield:3,than:2,thei:2,them:[0,2,5],thi:[0,2,5,9],those:2,time:[0,2],top:2,topic:9,type:[0,2,3,5],type_id:2,uniqu:2,updat:[0,2],upload:2,uploadedimag:[2,3],uploadimag:2,url:10,urlpattern:9,use:2,used:2,user:[0,1,2,3],user_id:[0,2],usernam:0,usernamefield:0,uses:2,using:[2,9],util:8,valu:[0,2,3,9],variabl:9,verbose_name_plur:3,via:2,view:[9,10],viewset:[0,2],want:2,websit:5,what:[2,5],when:[0,2],whether:2,which:2,who:2,widget:[0,5],width:[0,2],width_field:[0,2],work:2,wrapper:[0,2],write:2,wsgi:10,you:2},titles:["accounts package","accounts.migrations package","core package","core.migrations package","core.templatetags package","developer package","developer.migrations package","Welcome to Mega Backend Documentation\u2019s documentation!","manage module","mega_backend package","mega_backend"],titleterms:{"0001_initi":[1,3],account:[0,1],admin:[0,2,5],app:[0,2,5],asgi:9,backend:7,content:[0,1,2,3,4,5,6,9],core:[2,3,4],develop:[5,6],document:7,form:[0,5],indic:7,manag:8,mega:7,mega_backend:[9,10],migrat:[1,3,6],model:[0,2,5],modul:[0,1,2,3,4,5,6,8,9],packag:[0,1,2,3,4,5,6,9],permiss:2,serial:[0,2],set:9,signal:0,submodul:[0,1,2,3,5,9],subpackag:[0,2,5],tabl:7,templatetag:4,test:[0,2,5],url:[0,2,5,9],view:[0,2,5],welcom:7,wsgi:9}})