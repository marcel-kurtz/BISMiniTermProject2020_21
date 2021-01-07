# Data Thereatment 

## Soruce
All data is queryed form [statcube.at](https://statcube.at/statistik.at/ext/statcube/jsf/tableView/tableView.xhtml)

After downloading the data as .CSV the file is stored in `./raw`. Also a copy of the file should be stord in the `./processable` folder. In the copy, the data lines should be altered, so the description and decorative data is deleted. 

* TODO 
write script, which alters does data clearing automatically. 


## Directory Structure

- /data
    - /processable
    - /raw
- /graphics
    - /VisualizaionType
    - Python Script For Visualization .py
        - created graphs .png
- /models
    - Files for DataModelEntities .py
- /notebooks
    - notebooks with analysis .ipynb
    - scripts with analysis .py