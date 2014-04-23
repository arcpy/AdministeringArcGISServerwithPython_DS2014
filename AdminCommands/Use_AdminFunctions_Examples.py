    
import AdminFunctions
           
##### EXAMPLE CALLS TO FUNCTIONS INSIDE "AdminFunctions.py #####

CON = AdminFunctions.ADMINCON('admin', 'admin', 'arcola', 6080)

# Clear log files and change to Debug:
CON.modifyLogs(True, "DEBUG")

# Check on the token
CON.checkExpiredToken()

# Create a folder:
CON.createFolder("testServices", "Folder for test services")

# Get a list of folders and assign to a variable:
serverFolders = CON.getFolders()
print serverFolders

# Rename a service
CON.renameService("Buffer.GPServer", "BufferPolys")

# Stop, start or delete a service
serviceList = ["PolyCover.GPServer","BufferPolys.GPServer"]
CON.stopStartServices("Stop", serviceList)

# Get a list of services
serviceList = CON.getServiceList()
for service in serviceList:
    print service

# Get information about the server
CON.getServerInfo()

# Security...list users and roles
CON.securityReport()
CON.listRoles()
CON.listUsers()
CON.listUsersInRole("KevinUser")
CON.listUsersInRole("RestrictedPublishers")
CON.listRolesByUser("kevin")

# Backup the site to a directory
CON.exportSite(r"c:\arcgisserver")