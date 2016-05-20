import suds

url = 'http://localhost/cxwebinterface/portal/CxWebService.asmx?wsdl'
client = suds.client.Client(url)

login_applicationCredentials = client.factory.create('tns:Credentials') 
login_applicationCredentials.User = 'admin@cx' #cxUser Name
login_applicationCredentials.Pass = 'Qwe123$%^'#cxUser Pass

loginResponse = client.service.Login(login_applicationCredentials,2052)
cxSessionId = ''

if(loginResponse.IsSuccesfull):
    print('IsSuccesfull')
    print('SessionId = ' + loginResponse.SessionId)
    cxSessionId = loginResponse.SessionId
else:
    print(loginResponse.ErrorMessage)
    
project_name = 'project_git_py'
git_url = ''

team_id = '00000000-1111-1111-b111-989c9070eb11'

args = client.factory.create('tns:CliScanArgs') 

args_PrjSettings = client.factory.create('tns:ProjectSettings') 
args_PrjSettings.projectID = -1
args_PrjSettings.ProjectName = project_name
args_PrjSettings.PresetID = 1 #Preset All
args_PrjSettings.AssociatedGroupID = '00000000-1111-1111-b111-989c9070eb11' #Team CxServer
args_PrjSettings.ScanConfigurationID = 1 #Configuration Default
args_PrjSettings.Description = ''
args_PrjSettings.Owner = 'administrator' #string
args_PrjSettings.IsPublic = True

args_SrcCodeSettings = client.factory.create('tns:SourceCodeSettings') 
args_SrcCodeSettings.SourceOrigin = 'SourceControl' #Local,Shared,SourceControl,SourcePulling
# args_SrcCodeSettings.UserCredentials = tns:Credentials

#args_SrcCodeSettings.PathList = tns:ArrayOfScanPath

arg_src_sc = client.factory.create('tns:SourceControlSettings')

arg_src_sc.Port = 80
arg_src_sc.UseSSL = False
arg_src_sc.UseSSH = False
arg_src_sc.PerforceBrowsingMode = False
arg_src_sc.GitLsViewType = 'ALL'
arg_src_sc.Repository = 'GIT'
arg_src_sc.Protocol = 'PasswordServer'
arg_src_sc.ServerName = git_url
#arg_src_sc.RepositoryName


args_SrcCodeSettings.SourceControlSetting = arg_src_sc

# args_SrcCodeSettings.SourcePullingAction = tns:string
# args_SrcCodeSettings.SourceFilterLists = tns:SourceFilterLists
#arg_src_PackagedCode = client.factory.create('tns:LocalCodeContainer') 

#f = open(r'e:/jpfc9wmcd.zip', 'rb') #ziped sourceCode

#zipBase64Binary = base64.b64encode(f.read())
#f.close()

#print zipBase64Binary
#arg_src_PackagedCode.ZippedFile = zipBase64Binary #base64Binary
#arg_src_PackagedCode.FileName = 'abc.zip'

#args_SrcCodeSettings.PackagedCode = arg_src_PackagedCode


args.IsPrivateScan = False
args.IsIncremental = False
args.Comment = ''
args.IgnoreScanWithUnchangedCode = False
args.ClientOrigin = 'SDK'

isValidProjectNameResponse = client.service.IsValidProjectName(cxSessionId, project_name, team_id);
if(isValidProjectNameResponse.IsSuccesfull):
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
    
    sas = None
    
    pc_ScanActionSettings.ScanActionList = [pc_sa_ArrayOfScanAction] #Array of ArrayOfScanAction
    
    pc_ProjectIssueTrackingSettings = client.factory.create('tns:CxWSProjectIssueTrackingSettings') 
    
    pc_c_CxWSProjectCustomField = client.factory.create('tns:CxWSProjectCustomField') 
    
    pc_CustomFields = [pc_c_CxWSProjectCustomField] # Array of pc_c_CxWSProjectCustomField
    
    pc_DataRetentionSettings = client.factory.create('tns:DataRetentionSettings') 
    
    projectConfiguration.ScheduleSettings = pc_ScheduleSettings
    #projectConfiguration.ScanActionSettings = pc_ScanActionSettings
    projectConfiguration.ProjectIssueTrackingSettings = pc_ProjectIssueTrackingSettings
    projectConfiguration.CustomFields = pc_CustomFields
    projectConfiguration.DataRetentionSettings = pc_DataRetentionSettings
    pid = 0
    createNewProjectResponse = client.service.CreateNewProject(cxSessionId, projectConfiguration)
    if(createNewProjectResponse.IsSuccesfull):
        pid = createNewProjectResponse.ProjectID
        print pid
        #runScanWithExistingProjectResponse = client.service.RunScanWithExistingProject(cxSessionId, project_name)
        #runid = runScanWithExistingProjectResponse.RunId
    
    cxWSFilteredReportRequest = client.factory.create('tns:CxWSFilteredReportRequest')
    
    cxWSReportDisplayData = client.factory.create('tns:CxWSReportDisplayData')
    
    cxWSQueriesFilter = client.factory.create('tns:CxWSQueriesFilter');
    cxWSQueriesFilter.All = True
    cxWSQueriesFilter.IDs = []
    cxWSReportDisplayData.Queries = cxWSQueriesFilter
    
    cxWSResultsSeverityFilter = client.factory.create('tns:CxWSResultsSeverityFilter')
    cxWSResultsSeverityFilter.All = True
    cxWSResultsSeverityFilter.High = True
    cxWSResultsSeverityFilter.Medium = True
    cxWSResultsSeverityFilter.Low = True
    cxWSResultsSeverityFilter.Info = True
    cxWSReportDisplayData.ResultsSeverity = cxWSResultsSeverityFilter
    
    cxWSResultsStateFilter = client.factory.create('tns:CxWSResultsStateFilter')
    cxWSResultsStateFilter.All = True
    cxWSResultsStateFilter.IDs = []
    cxWSReportDisplayData.ResultsState = cxWSResultsStateFilter
    
    cxWSDisplayCategoriesFilter = client.factory.create('tns:CxWSDisplayCategoriesFilter')
    cxWSDisplayCategoriesFilter.All = True
    cxWSDisplayCategoriesFilter.IDs = []
    cxWSReportDisplayData.DisplayCategories = cxWSDisplayCategoriesFilter
    
    cxWSResultsAssignedToFilter = client.factory.create('tns:CxWSResultsAssignedToFilter')
    cxWSResultsAssignedToFilter.All = True
    cxWSResultsAssignedToFilter.IDs = []
    cxWSResultsAssignedToFilter.Usernames = []
    cxWSReportDisplayData.ResultsAssigedTo = cxWSResultsAssignedToFilter
    
    cxWSResultsPerVulnerabilityFilter = client.factory.create('tns:CxWSResultsPerVulnerabilityFilter')
    cxWSResultsPerVulnerabilityFilter.All = True
    cxWSResultsPerVulnerabilityFilter.Maximimum = 3
    cxWSReportDisplayData.ResultsPerVulnerability = cxWSResultsPerVulnerabilityFilter
    
    cxWSHeaderDisplayOptions = client.factory.create('tns:CxWSHeaderDisplayOptions')
    cxWSHeaderDisplayOptions.Link2OnlineResults = True
    cxWSHeaderDisplayOptions.Team = True
    cxWSHeaderDisplayOptions.CheckmarxVersion = True
    cxWSHeaderDisplayOptions.ScanComments = True
    cxWSHeaderDisplayOptions.ScanType = True
    cxWSHeaderDisplayOptions.SourceOrigin = True
    cxWSHeaderDisplayOptions.ScanDensity = True
    cxWSReportDisplayData.HeaderOptions = cxWSHeaderDisplayOptions
    
    cxWSGeneralDisplayOptions = client.factory.create('tns:CxWSGeneralDisplayOptions')
    cxWSGeneralDisplayOptions.OnlyExecutiveSummary = True
    cxWSGeneralDisplayOptions.TableOfContents = True
    cxWSGeneralDisplayOptions.ExecutiveSummary = True
    cxWSGeneralDisplayOptions.DisplayCategories = True
    cxWSGeneralDisplayOptions.DisplayLanguageHashNumber = True
    cxWSGeneralDisplayOptions.ScannedQueries = True
    cxWSGeneralDisplayOptions.ScannedFiles = True
    cxWSGeneralDisplayOptions.VulnerabilitiesDescription = 'None'#None,Attached2Appendix,Linked2Online
    cxWSReportDisplayData.GeneralOption = cxWSGeneralDisplayOptions
    
    cxWSResultDisplayOptions = client.factory.create('tns:CxWSResultDisplayOptions')
    cxWSResultDisplayOptions.AssignedTo = True
    cxWSResultDisplayOptions.Comments = True
    cxWSResultDisplayOptions.Link2Online = True
    cxWSResultDisplayOptions.ResultDescription = True
    cxWSResultDisplayOptions.SnippetsMode = 'None'#None,SourceAndDestination,Full
    cxWSReportDisplayData.ResultsDisplayOption = cxWSResultDisplayOptions
    
    cxWSFilteredReportRequest.Type = 'PDF'
    cxWSFilteredReportRequest.ScanId = 1
    cxWSFilteredReportRequest.DisplayData = cxWSReportDisplayData
    
    createScanReportResponse = client.service.CreateScanReport(cxSessionId, cxWSFilteredReportRequest)
print  'ok'