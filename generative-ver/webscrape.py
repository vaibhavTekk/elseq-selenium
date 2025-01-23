"""
    Web element scraping version. This relies on a typical langauage model that 
    generates summaries of a given site using a dataframe with relevant parameters 
    of all interactive webelements. scrape_site() returns a dataframe with the
    relevant parameters. generate_summary() returns a summary of the site.
    generate_testcases() creates a script of testcases based on the summary.
"""

def scrape_site(url):
    """Scrapes a given URL and returns a dataframe with relevant parameters of all interactive webelements.
    
    Args:
        url: str
    
    Returns:
        DataFrame: A Pandas DataFrame containing the relevant parameters of all interactive webelements.
    """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import pandas as pd
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    # Step 4: Find all interactive elements
    interactive_elements = driver.find_elements(By.XPATH, '//a | //button | //input | //select | //textarea')

    # Step 5: Extract relevant parameters
    data = []
    for element in interactive_elements:
        element_data = {
            'tag_name': element.tag_name,
            'type': element.get_attribute('type'),
            'id': element.get_attribute('id'),
            'name': element.get_attribute('name'),
            'class': element.get_attribute('class'),
            'text': element.text,
            'xpath': driver.execute_script("""
                function getElementXPath(element) {
                    if (element.id !== '') {
                        return 'id("' + element.id + '")';
                    }
                    if (element === document.body) {
                        return element.tagName;
                    }
                    var ix = 0;
                    var siblings = element.parentNode.childNodes;
                    for (var i = 0; i < siblings.length; i++) {
                        var sibling = siblings[i];
                        if (sibling === element) {
                            return getElementXPath(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
                        }
                        if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                            ix++;
                        }
                    }
                }
                return getElementXPath(arguments[0]);
            """, element),
            'coordinates': element.location,
            'label': element.get_attribute('aria-label') or element.get_attribute('label') or element.get_attribute('placeholder'),
            'role' : element.get_attribute('role') or element.get_attribute('aria-role'),
        }
        data.append(element_data)

    df = pd.DataFrame(data)
    return df

def generate_summary(df):
    """Generates a summary of the website using the given dataframe, suitable for feeding 
    as context to code generation models that can generate appropriate test cases for webelements 
    from the given page.

    Args:
        df (DataFrame): A Pandas DataFrame containing the relevant parameters of all interactive webelements.

    Returns:
        str: A summary of the website.
    """
    from ollama import chat
    # Prepare the messages for the chat
    messages = [
        {
            'role': 'user',
            'content': f"Generate a summary of the website using the given dataframe, which includes relevant parameters of all interactive webelements such as element type, attributes, and actions. The summary should be clear and comprehensive, providing a detailed description of the webpage's structure and functionality, suitable for generating appropriate test cases for the webelements. Assume this response will directly be fed to code generation models that generate test cases accordingly. When mentionining potential test cases, mention the dataframe index of the relevant elements, to help with automatically generating testcases. {df.to_string()}",
        },
    ]

    # Query the model
    response = chat('llama3.2', messages=messages)

    # Print the response
    return response['message']['content']


def generate_testcases(summary, df):
    """Generates a test script that includes test cases for the interactive elements 
    on the webpage based on the given summary.

    Args:
        summary (str): An AI generated summary of the website
        df (DataFrame): A Pandas DataFrame containing the relevant parameters of all interactive webelements.
    
    Returns:
        str: A test script that includes test cases for the interactive elements on the webpage.
    """
    
    # from ollama import Client
    # client = Client()
    # response = client.create(
    #     'model' : 'codegen',
    #     'task' : 'testcase_generation',
    #     'from_': 'llama3.2',
    #     'system': 'You are a code generator that reads a given summary of a website and generates a python->selenium script that tests the interactive elements on the webpage.',
    #     'stream': False
    # )
    
    # print(response.status)
    # print("Model generated, generating script...")
    
    from ollama import chat
    messages = [
        {
            'role': 'user',
            'content': f"Generate a python->selenium test script for a website that has been summarized below. Summary: {summary} Dataframe: {df.to_string()}",
        },
    ]
    response = chat('llama3.2', messages=messages)
    return response['message']['content']

print("Scraping site...", end = "")
df = scrape_site("http://ec2-52-32-108-4.us-west-2.compute.amazonaws.com:8082/")
print("Done!\n-----\n")
print("Generating summary and test script...\n")
summary = generate_summary(df)
print(summary)
test_script = generate_testcases(summary, df)
print(test_script)