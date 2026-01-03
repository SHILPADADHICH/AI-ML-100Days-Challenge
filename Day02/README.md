### Day 2 – 100 Days of AI/ML Challenge

**What I Learned Today**

### Python Basics

Learning Python feels like learning a new language.

*   First, you learn the **words** → variables and data types
    
*   Then, you learn how to form **sentences** → operators and expressions
    
*   Finally, you understand the **grammar** → control flow
    

Once these basics are clear, everything else in Python starts making sense.

### Python’s Unique Feature: Indentation

One thing that makes Python different from many other languages is **indentation**.

Most programming languages use {} brackets to define code blocks, but Python uses **spaces**.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Python – clean and readable  if temperature > 30:      print("It's hot!")      print("Turn on AC")   `

In comparison, languages like JavaScript use braces:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   if (temperature > 30) {      console.log("It's hot!");      console.log("Turn on AC");  }   `

### Indentation Rules

Indentation must be **consistent** in Python.

Correct usage with 4 spaces:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   if score > 90:      print("A grade")      if score == 100:          print("Perfect!")   `

Incorrect usage with mixed spaces:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   if score > 90:    print("A grade")    # 2 spaces      if score == 100:  # 4 spaces        print("Perfect!")  # 6 spaces   `

If indentation is wrong, **Python won’t run at all**.This is the **most common beginner mistake**.

### Python Syntax

Syntax simply means **the rules of writing Python code**.

For now, the most important things to remember are:

*   Python cares about **spelling**
    
*   Python cares about **order**
    
*   Python cares **a lot** about **indentation**
    

As you continue learning, these rules will become second nature.

### PEP8 – Python Styling Guide

PEP8 is Python’s official style guide. It explains best practices such as:

*   Using **4 spaces** for indentation (not tabs)
    
*   Keeping lines under **79 characters**
    
*   Following proper naming conventions (user\_name instead of userName)
    
*   Adding spaces around operators for readability
    

### Python Errors

**Understanding When Code Doesn’t Run**

When you break Python’s rules, your code stops running and Python shows an **error message**.

At first, this feels frustrating. But errors are actually helpful because they:

*   Tell you **what went wrong**
    
*   Show **where** the problem happened
    

### Errors Are Normal

Every programmer—beginner or expert—faces errors daily.

The only difference is experience:

*   Beginners fear errors
    
*   Experts have learned from hundreds of them
    

With practice, error messages start feeling like **road signs**, not warnings.

### Using AI to Fix Errors

When you’re stuck:

1.  Copy the **entire error message**
    
2.  Paste it into ChatGPT, Claude, or another AI tool
    
3.  Share your code for context
    

AI tools are great at explaining errors and suggesting fixes.Even experienced developers rely on them—**it’s a tool, not cheating**.

### Variables

**Storing and Naming Data**

Variables let you store information so you can reuse it later.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   name = "Alice"  age = 25  is_student = True   `

Here’s what’s happening:

*   name is the variable
    
*   \= means “store”
    
*   "Alice" is the value being stored
    

### Variable Naming Rules

Python follows specific rules for naming variables.

Valid examples:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   user_name = "Dave"  userName = "Dave"  age2 = 30  _private = "secret"   `

Invalid examples:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   2age = 30  my-name = "Dave"  my name = "Dave"  class = "Python"   `

### Difference Between = and ==

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # = is used to assign a value  age = 25  # == is used to compare values  if age == 25:      print("Quarter century!")   `

### Python Naming Convention

Python uses **snake\_case**, which means lowercase words separated by underscores.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   first_name = "Alice"  user_age = 25  is_logged_in = True  shopping_cart_total = 49.99   `

### Data Types

**Different Kinds of Information**

Python works with different types of data.You can’t treat everything the same way—just like real life.

Main data types:

*   **Numbers** for calculations
    
*   **Strings** for text
    
*   **Booleans** for decisions
    

Each type behaves differently.

### Why Data Types Matter

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Numbers can do math  total = 10 + 5  # Strings join together  name = "Hello" + "World"  # Mixing types causes errors  # age = "25" + 5  age = int("25") + 5   `

### Types of Numbers in Python

**Integers** (whole numbers):

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   age = 25  score = -10   `

**Floats** (decimal numbers):

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   price = 19.99  temperature = -5.5  pi = 3.14159   `

Python uses a **dot (.)** for decimals.Using 3,14 creates a tuple, not a number.

### Strings

**Working With Text**

Strings are text written inside quotes.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   message = "Hello"  greeting = 'Hi'   `

Python doesn’t care whether you use single or double quotes—just be consistent.

Practicing string operations helps build confidence.

### Booleans

**True or False Values**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   is_logged_in = True  is_admin = False  has_permission = True   `

Boolean values must be written as **True** or **False**.Using lowercase true or false will cause an error.

Booleans represent **yes/no decisions**.

### Operators

**Math, Comparison, and Logic**

Operators make things happen in code.

*   Math operators: +, -, \*, /
    
*   Comparison operators: >, <, ==
    
*   Logical operators: and, or, not
    

### String Manipulation

**Advanced Text Operations**

Python provides many built-in string methods that help you:

*   Modify text
    
*   Search patterns
    
*   Clean messy data
    

Examples:

*   upper() → converts text to uppercase
    
*   replace() → replaces parts of text
    

Most string methods are easy to understand just by reading their names.