import gitlab


gl = gitlab.Gitlab()

# list all the projects
projects = gl.projects.list(iterator=True, topic='pytest')
for project in projects:
    print(project)
    break

