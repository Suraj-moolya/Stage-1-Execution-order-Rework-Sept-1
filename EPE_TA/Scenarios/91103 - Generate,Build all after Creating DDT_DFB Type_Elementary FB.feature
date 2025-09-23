Feature: 91103 - To test Generate, Incremental generate, Build and Build all Functionality after Creating Derived Data Type_Derived FB Type_Elementary FB Instances_ Derived FB Instances

















######################################################################################################################
#Execution order for tc-91103
###################################################
#Scenarios\nn Refine Online\Refine Online of Controllers
#Scenarios\78 Open refine online and check the build and deploy functionality - Close Refine online window and yes on popup
#Scenarios\145 Check existing Excutable Status(if it is in build state, open refine)
#tag-@TC_verify_outofdate
#tag-@Generate_M580_Standalone_controlproject
#tag-@verify_built_for_m580_standalone
#Scenario\146 Build_Build all the existing executable(if any errors found, clear and build)
#tags-@GenerateAndBuild_ControlEcecutable_1
#Scenario Outline: Build All from control executeable r-click