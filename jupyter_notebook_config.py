# Based on gfyoung's jupyterlab-heroku repo

# Supposedly, as long as our notebook resides on the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False

# More information about SSL and heroku: # https://devcenter.heroku.com/articles/ssl-endpoint