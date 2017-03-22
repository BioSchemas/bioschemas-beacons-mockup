# Objective
This is a Proof of Concept to show how [Beacons](https://genomicsandhealth.org/work-products-demonstration-projects/beacon-project-0) can expose [Schema.org](http://schema.org) markup and how Schema.org metadata annotations can be easily harvested to automatically maintain an updated beacon registry.

# Requirements
For this Proof of concept to work you will need:
1. Homebrew installed. [Installation](https://brew.sh/)
2. Python 3 with virtual environment installed. [Installation](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
3. Scrapy installed. [Documentation](https://doc.scrapy.org/en/latest/intro/tutorial.html)
4. Install Extruct. [Installation](https://github.com/scrapinghub/extruct)
5. Install a Web Server as [XAMPP](https://www.apachefriends.org/index.html) to host modified beacon's pages.
6. Test your Web Pages Modifications [Google Schema Validator](https://search.google.com/structured-data/testing-tool)

# Schema.org markup
For this mock up we did chose the [DataCatalog schema.org type](http://schema.org/DataCatalog) and just few properties to prove the concept.
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Beacon Sample Structure</title>
  </head>
  <body>
    <div vocab="http://Schema.org/" typeof="DataCatalog" class="main-container">
      <h1 property="name">Beacon's Name</h1>
      <span property="description">Here you put the Beacon's despcription</span>
      <select typeof="DataSet" property="dataset">
          <option property="name" value="dataset_name_1">dataset_name_1</option>
          <option property="name" value="dataset_name_2">dataset_name_2</option>
          <option property="name" value="dataset_name_3">dataset_name_3</option>
          <option property="name" value="dataset_name_4">dataset_name_4</option>
      </select>
      <span property="version">API version 0.0.0</span>
    </div>
  </body>
</html>
```
# Beacon mockup Schema.org markup
![Sample of GA4GH Beacon with ](http://gdurl.com/SI21)

# Collection of metadata into a registry
Process we followed to integrate metadata from several beacons mockups
![Image of Beacon - Registry Project](http://gdurl.com/MJFd)

# Test Code
Steps to reproduce this proof of concept
1. Download beacon’s pages with schema, folder: beacons_pages_schema.
2. Host this folder in your localhost httpdocs directory of XAMPP
3. Download Python 3 virtual environment folder: python_code 
4. Create in python_code directory a folder called `beacon_registry` -> `mkdir beacon_registry`.
5. Open terminal or Console make a virtual environment called `beacon_registry` with the following command `pyvenv beacon_registry`
6. Go to python_code folder an execute `beacon_registry/bin/activate`
7. Execute spider `beacon_spider.py` located at [`bioschemas-beacons-mockup/python_code/beacon_spyder/beacon_spyder/spiders/`](https://github.com/BioSchemas/bioschemas-beacons-mockup/tree/master/python_code/beacon_spyder/beacon_spyder/spiders)
8. Open `index.html` file created at the [`bioschemas-beacons-mockup/results_page/`](https://github.com/BioSchemas/bioschemas-beacons-mockup/tree/master/results_page) directory.

# Support or Contact
For futher information [contact](mailto:guillermo.calderon@elixir-europe.org) or @guicalman.
