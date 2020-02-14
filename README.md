# Introduction

Recommend Me, is a movie recommender system, recommendation based on content (already existed movies data) and matching function based on cosine similarity. The service is connected with FLASK REST API and respond through an HTTP request. 
Here are the details:

# Cosine similarity
The dot product between two vectors is equal to the projection of one of them on the other.

![Activity](https://github.com/Hassan-json/Recommend-Me/blob/master/images/1_kDWCM-8qopE2ekudxlOudw.png)
![Activity](https://github.com/Hassan-json/Recommend-Me/blob/master/images/1_JdXBbKlOKS9UNFpLNchfdA.png)
![Activity](https://github.com/Hassan-json/Recommend-Me/blob/master/images/1_JDlFeJM-Z3VQFprHGBTd9A.png)

# Gather the data

```
data = pd.read_csv('../data_files/data.csv')
    
```
# Data Cleaning 

```

df['Key_words'] = ""

for index, row in df.iterrows():
    plot = row['Plot']
    
    # instantiating Rake, by default it uses english stopwords from NLTK
    # and discards all puntuation characters as well
    r = Rake()

    # extracting the words by passing the text
    r.extract_keywords_from_text(plot)

    # getting the dictionary whith key words as keys and their scores as values
    key_words_dict_scores = r.get_word_degrees()
    
    # assigning the key words to the new column for the corresponding movie
    row['Key_words'] = list(key_words_dict_scores.keys())

df.drop(columns = ['Plot'], inplace = True)

```

# UML

Following are the UML diagrams of the project.

### 1. Activity Diagram
![Activity](https://github.com/Hassan-json/Recommend-Me/blob/master/images/2.PNG)

### 2. Use Case Diagram
![Use Case](https://github.com/Hassan-json/Recommend-Me/blob/master/images/1.PNG)

### 3. Deployment Diagram
![Deployment](https://github.com/Hassan-json/Recommend-Me/blob/master/images/3.PNG)

# Metrics

For the code analysis and review, the industry standard tool, &quot;SonarQube&quot; was used. Initially code smell was significantly higher, which was gradually mitigated by applying refactoring techniques.

Please note that during code analysis, source codes from 3rd party libraries (e.g. object detection module from TensorFlow) were excluded.

For Example;
- In one case, a large code block was broken down into smaller code blocks, hence reducing code complexity.
- Function parameters were increased/decreased for making method calls more simpler and easier.
- Logically related pieces of code were merged together under same functions.

Software metrics that were monitor during course of development were;

![Context Management Usage](https://github.com/Hassan-json/Recommend-Me/blob/master/images/screencapture-localhost-9000-dashboard-1581469959797.png)
![Context Management Usage](https://github.com/Hassan-json/Recommend-Me/blob/master/images/screencapture-localhost-9000-project-activity-1581470237478.png)
![Context Management Usage](https://github.com/Hassan-json/Recommend-Me/blob/master/images/screencapture-localhost-9000-component_measures-1581470180203.png)
![Context Management Usage](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Sonar.PNG)


# Clean Code Development

### 1. Consistent naming convention
Throughout coding, naming scheme of camel case is used for both variables and functions. Moreover, for immutable/final variables all-upper-casing scheme is used.

### 2. Minimizing of Side-Effect using Context Management
Wherever necessary, side-effects have been tried to minimized by isolating its effect at local scope by making use of python&#39;s context management.

```
from src.POM_Unit_Tests.Locators import Locators
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.movieNameText_name = Locators.Locators.movieNameText_name
        self.searchBtn_name = Locators.Locators.searchBtn_name
```


### 3. Modularity
Source code has been divided into two modules. Module &quot;Analyzer&quot; is responsible for object recognition tasks, while module &quot;Router&quot; is responsible for routing of incoming and outgoing rest API requests.

![Module Analyzer(analyzer.py) being imported in Module Router(app.py)](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Capture_new.PNG)

### 4. Exception Handling
Wherever necessary exception handling blocks have been added to ensure that no runtime errors are thrown.

![Exception Handling](https://github.com/Hassan-json/Recommend-Me/blob/master/images/capture_01.PNG)

Exception Handling Usage

### 5. Configurable Data at Higher Level
All configurable data (for example: Directory names, paths), have been placed at higher level, making tweaking of values easier for the purpose of debugging.

![Configurable Data](https://github.com/Hassan-json/Recommend-Me/blob/master/images/libs.PNG)

Configurable Data and Constants at higher level

# Continuous Delivery

Continuous Delivery and integration pipeline of this project is based on Jenkins. 

![Jenkins](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Jenkins%20-%20Home.PNG)
![Jenkins](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Jenkins%20-%20Console%20output.PNG)

# Unit Testing 
### POM Project Model
![POM](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Page-Object-Model-Framework.png)

### POM Directory Structure 

![POM](https://github.com/Hassan-json/Recommend-Me/blob/master/images/POM.PNG)

### POM Unit Case Class 

![POM](https://github.com/Hassan-json/Recommend-Me/blob/master/images/POM%20unit%20test.PNG)

### Selenium 

![POM](https://github.com/Hassan-json/Recommend-Me/blob/master/images/selenium.png)
![POM](https://github.com/Hassan-json/Recommend-Me/blob/master/images/POM.PNG)

### Git BASH 

![GIT](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Capture.PNG)

# IDE for Developemnet 
IntelliJ Cheat Sheet

![GIT](https://github.com/Hassan-json/Recommend-Me/blob/master/images/IntelliJ-cheat-sheet-part-1.jpg)


# Build Management (+ DSL)

For the purposes of build management this project is dependent on Gradle and IML file 

![GIT](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Gradle.PNG)

Following script is also an example of Domain Specific Language. This script has been written in .iml.

![GIT](https://github.com/Hassan-json/Recommend-Me/blob/master/images/iml.PNG)

Directory Structure

![GIT](https://github.com/Hassan-json/Recommend-Me/blob/master/images/files.PNG)



# Functional Programming

Throughout this project, good practices for functional programming have been adopted. Following are few examples of such practices;

### 1. Final Data Structures Usage
Few variables have been made made immutable in code. Hence using as constant.

```
cv = CountVectorizer()
count_matrix = cv.fit_transform(data['comb'])
sim = cosine_similarity(count_matrix)
np.save('similarity_matrix', sim)
data.to_csv('D:/CS4DS & SWT++/Recommend-Me/data_files/data.csv',index=False)
```

### 2. Side Effect Free Functions
As discussed earlier, wherever necessary context management has been used. So that effect of overlying function could remain locally. Hence using them would not result any side effects.

![Side Effect Free](https://github.com/Hassan-json/Recommend-Me/blob/master/images/Capture_new.PNG)


### 3. Use of higher order functions
Higher order functions like map and filter have also been used.

![Higher Order Function](https://github.com/Hassan-json/Recommend-Me/blob/master/images/hof.PNG)

### 4. Clojures/Anonymous Functions

Usage of anonymous functions like &quot;Lambda&quot; have also been made, for getting rid from unnecessary function signature bodies where required.

![Anonymous Function](https://github.com/Hassan-json/Recommend-Me/blob/master/images/lamda.PNG)
