import suds
import base64

url = 'http://localhost/cxwebinterface/sdk/CxSDKWebService.asmx?wsdl'
client = suds.client.Client(url)

cxSessionId = ''
args = client.factory.create('tns:CliScanArgs') 

args_PrjSettings = client.factory.create('tns:ProjectSettings') 
args_PrjSettings.projectID = -1
args_PrjSettings.ProjectName = 'test_from_py'
args_PrjSettings.PresetID = 1 #Preset All
args_PrjSettings.AssociatedGroupID = '00000000-1111-1111-b111-989c9070eb11' #Team CxServer
args_PrjSettings.ScanConfigurationID = 1 #Configuration Default
args_PrjSettings.Description = ''
args_PrjSettings.Owner = 'administrator' #string
args_PrjSettings.IsPublic = True

args_SrcCodeSettings = client.factory.create('tns:SourceCodeSettings') 
args_SrcCodeSettings.SourceOrigin = 'Local' #Local,Shared,SourceControl,SourcePulling
# args_SrcCodeSettings.UserCredentials = tns:Credentials
# args_SrcCodeSettings.PathList = tns:ArrayOfScanPath
# args_SrcCodeSettings.SourceControlSetting = tns:SourceControlSettings
# args_SrcCodeSettings.SourcePullingAction = tns:string
# args_SrcCodeSettings.SourceFilterLists = tns:SourceFilterLists
arg_src_PackagedCode = client.factory.create('tns:LocalCodeContainer') 

f = open(r'e:/jpfc9wmcd.zip', 'rb') #ziped sourceCode

zipBase64Binary = base64.b64encode(f.read())
f.close()

#print zipBase64Binary
arg_src_PackagedCode.ZippedFile = zipBase64Binary #base64Binary
arg_src_PackagedCode.FileName = 'abc.zip'

args_SrcCodeSettings.PackagedCode = arg_src_PackagedCode


args.IsPrivateScan = False
args.IsIncremental = False
args.Comment = ''
args.IgnoreScanWithUnchangedCode = False
args.ClientOrigin = 'SDK'

#print client

projectConfiguration = client.factory.create('tns:ProjectConfiguration') 
projectConfiguration.ProjectSettings = args_PrjSettings
projectConfiguration.SourceCodeSettings = args_SrcCodeSettings

pc_ScheduleSettings = client.factory.create('tns:ScheduleSettings') 
pc_ScheduleSettings.Schedule = 'None' #None,Now,Weekly

pc_ScanActionSettings = client.factory.create('tns:ScanActionSettings') 

pc_sa_ArrayOfScanAction = client.factory.create('tns:ArrayOfScanAction') 

sa = client.factory.create('tns:ScanAction') 
sa.Parameters = ['770548531@qq.com']
sa.Trigger = 'AfterScanSucceeds' #BeforeScanStarts,AfterScanSucceeds,OnScanFailure
sa.Action = 'EmailNotification' #EmailNotification,PostScanAction
pc_sa_ArrayOfScanAction.ScanAction = sa

pc_ScanActionSettings.ScanActionList = [pc_sa_ArrayOfScanAction] #Array of ArrayOfScanAction

pc_ProjectIssueTrackingSettings = client.factory.create('tns:CxWSProjectIssueTrackingSettings') 

pc_c_CxWSProjectCustomField = client.factory.create('tns:CxWSProjectCustomField') 

pc_CustomFields = [pc_c_CxWSProjectCustomField] # Array of pc_c_CxWSProjectCustomField

pc_DataRetentionSettings = client.factory.create('tns:DataRetentionSettings') 

projectConfiguration.ScheduleSettings = pc_ScheduleSettings
projectConfiguration.ScanActionSettings = pc_ScanActionSettings
projectConfiguration.ProjectIssueTrackingSettings = pc_ProjectIssueTrackingSettings
projectConfiguration.CustomFields = pc_CustomFields
projectConfiguration.DataRetentionSettings = pc_DataRetentionSettings

#projectConfiguration unused
#print projectConfiguration

#login
login_applicationCredentials = client.factory.create('tns:Credentials') 
login_applicationCredentials.User = 'admin@cx' #cxUser Name
login_applicationCredentials.Pass = 'Qwe123$%^'#cxUser Pass

loginResponse = client.service.Login(login_applicationCredentials, 2052)
if(loginResponse.IsSuccesfull):
    print('IsSuccesfull')
    print('SessionId = ' + loginResponse.SessionId)
    cxSessionId = loginResponse.SessionId
else:
    print(loginResponse.ErrorMessage)
#scan

url2 = 'http://localhost/cxwebinterface/portal/CxWebService.asmx?wsdl'
client2 = suds.client.Client(url2)
print client2
#scanResponse = client.service.Scan(cxSessionId, args)

#print loginResponse
