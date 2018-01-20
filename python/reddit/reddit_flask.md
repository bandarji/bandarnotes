```python
import os.path, time
from datetime import datetime

#Get current time
current_time = time.localtime()
current_time2 = time.strftime('%m/%d/%Y', )
print(current_time2)

#Get modified time of Sans.db
modified_time2 = time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime("sans.db")))
print(modified_time2)

#if todays date
if modified_time2 == current_time2:
    print("do this")

#create table
else:
    print("it is not todays date...")
```

this works currently, but if it's todays date, i want it to skip the making the
database and just load the html page

```python
import sqlite3, os, warnings, pandas as pd, os.path, time
from flask import Flask, g, render_template
from contextlib import closing
from datetime import datetime

warnings.filterwarnings('ignore')

# create our little application :)
app = Flask(__name__)

@app.route('/')
def stacked_bar_chart():


        # load data
        df = pd.read_csv('auditreport2.csv')

        # strip whitespace from headers
        df.columns = df.columns.str.strip()
        con = sqlite3.connect("sans.db")

        # drop data into database
        df.to_sql("MyTable", con, if_exists='replace')

        # Print total of incomplete
        qry = """
        SELECT Total FROM
        (
        select distinct 
            [Employee Department] as Department
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]='Incomplete' AND [Curriculum Name] NOT LIKE '%Phishing Training%' AND `Curriculum Name` NOT LIKE '%ARB Developer Training%' ) as Total
        from MyTable t1 ORDER BY Department ASC
        )
        """

        # Print users that have not completed training to dataframe
        qry2 = """
        SELECT [Employee Name], [Employee Department], [Curriculum Name], [Date Assigned] FROM MyTable Where [Completion Status] = 'Incomplete' ORDER BY [Employee Department] ASC    """

        # Print label for graph #
        qry3 = """
        Select distinct [Employee Department] 
        FROM MyTable
        ORDER BY [Employee Department] ASC
        """

        # Print total of complete for stacked bargraph
        qry5 = """
        SELECT Total FROM
        (
        select distinct 
            [Employee Department]
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]=' Complete' AND `Curriculum Name` NOT LIKE '%Phishing%' AND `Curriculum Name` NOT LIKE '%ARB Developer Training%' AND [Date Assigned] > date('NOW', '-30 day')) as Total
        from MyTable t1 ORDER BY [Employee Department] ASC
        )
        """

        # incomplete_Phishing
        qry6 = """
            SELECT Total FROM
        (
        select distinct 
            [Employee Department]
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]='Incomplete' AND `Curriculum Name` NOT LIKE '%CARB Security Training%' AND `Curriculum Name` NOT LIKE '%ARB Developer Training%' AND `Curriculum Name` NOT LIKE '%OIS Support Training%' AND `Curriculum Name` NOT LIKE '%Legal EO Training%') as Total
        from MyTable t1 ORDER BY [Employee Department] ASC
        )
        """

        # complete_Phishing
        qry7 = """
            SELECT Total FROM
        (
        select distinct 
            [Employee Department]
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]=' Complete' AND `Curriculum Name` NOT LIKE '%CARB Security Training%' AND `Curriculum Name` NOT LIKE '%ARB Developer Training%' AND `Curriculum Name` NOT LIKE '%OIS Support Training%' AND `Curriculum Name` NOT LIKE '%Legal EO Training%') as Total
        from MyTable t1 ORDER BY [Employee Department] ASC
        )
        """

        # incomplete_dev
        qry8 = """
        SELECT Total FROM
        (
        select distinct 
            [Employee Department]
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]='Incomplete' AND `Curriculum Name` NOT LIKE '%CARB Security Training%' AND `Curriculum Name` NOT LIKE '%Phishing Training%' AND `Curriculum Name` NOT LIKE '%OIS Support Training%' AND `Curriculum Name` NOT LIKE '%Legal EO Training%' AND [Date Assigned] < date('NOW', '-30 day')) as Total
        from MyTable t1 ORDER BY [Employee Department] ASC
        )
        """

        # complete_dev
        qry9 = """
                SELECT Total FROM
        (
        select distinct 
            [Employee Department]
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]=' Complete' AND `Curriculum Name` NOT LIKE '%CARB Security Training%' AND `Curriculum Name` NOT LIKE '%Phishing Training%' AND `Curriculum Name` NOT LIKE '%OIS Support Training%' AND `Curriculum Name` NOT LIKE '%Legal EO Training%' AND [Date Assigned] > date('NOW', '-30 day')) as Total
        from MyTable t1 ORDER BY [Employee Department] ASC
        )
        """

        # new users < 30 days
        qry10 = """
        SELECT Total FROM
        (
        select distinct 
            [Employee Department] as Department
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]='Incomplete' AND [Curriculum Name] NOT LIKE '%Phishing Training%' AND [Date Assigned] < date('NOW', '-30 day')) as Total
        from MyTable t1 ORDER BY Department ASC
        )
        """
        # new users < 30 days complete
        qry11 = """
        SELECT Total FROM
        (
        select distinct 
            [Employee Department] as Department
            ,(select count(*) from MyTable t2 where t2.[Employee Department] = t1.[Employee Department] AND t2.[Completion Status]='Incomplete' AND [Curriculum Name] NOT LIKE '%Phishing Training%' AND [Date Assigned]  > date('now','-30 day')) as Total
        from MyTable t1 ORDER BY Department ASC
        )
        """

        # convert sql query to readable databaframe #
        df = pd.read_sql_query(qry, con)
        df5 = pd.read_sql_query(qry5, con)
        df1 = pd.read_sql_query(qry2, con) 
        df2 = pd.read_sql_query(qry3, con)
        df6 = pd.read_sql_query(qry6, con)
        df7 = pd.read_sql_query(qry7, con)
        df8 = pd.read_sql_query(qry8, con)
        df9 = pd.read_sql_query(qry9, con)
        df10 = pd.read_sql_query(qry10, con)
        df11 = pd.read_sql_query(qry11, con)

        # convert dataframes to lists readable to chartjs #
        complete = df5.values.flatten().tolist()
        incomplete = df.values.flatten().tolist()
        department = df2.values.flatten().tolist()
        incomplete_phishing = df6.values.flatten().tolist()
        complete_phishing = df7.values.flatten().tolist()
        incomplete_dev = df8.values.flatten().tolist()
        complete_dev = df9.values.flatten().tolist()
        thirtydaysIncomplete = df10.values.flatten().tolist()
        thirtydaysComplete = df11.values.flatten().tolist()


        # variable for html output
        df1.index = df1.index + 1
        df1.style
        list_of_users = df1

        print(complete_phishing)
        print(incomplete_phishing)

        return render_template('index.html', incomplete=incomplete, complete=complete, department=department, incomplete_phishing=incomplete_phishing, complete_phishing=complete_phishing, incomplete_dev=incomplete_dev, complete_dev=complete_dev, thirtydaysIncomplete=thirtydaysIncomplete, thirtydaysComplete=thirtydaysComplete, list_of_users=list_of_users.to_html())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

```python
# could be shortened (and increase performance) by doing :
qry = """
    select 
        [Employee Department] as Department
        , count(*) AS Total
    FROM MyTable 
    WHERE [Completion Status]='Incomplete' 
    AND [Curriculum Name] NOT LIKE '%Phishing Training%' 
    AND [Curriculum Name] NOT LIKE '%ARB Developer Training%' 
    GROUP BY Department 
    ORDER BY Department

    """
```
