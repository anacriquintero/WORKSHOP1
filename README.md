<h1 align="center">ETL-Candidates-Job-Data-Doc</h1>


<h2>Description</h2>

<p>
A project to practice technical knowledge using:
<b>SQL - Python - Git - GitHub - Notebooks - Clean Code</b>
</p>

<h3>Exploratory Data Analysis (EDA)</h3>

<p>
In this project, we perform an analysis of the dataset to identify the type of columns, detect dispersion, and identify outliers. This process ensures that the data is clean, organized, and free of atypical values.
</p>

<h3>Final Product</h3>

<p>
As a result, we obtain visualizations and create a dashboard that extracts value from the dataset's information.
</p>

<h4>Some of the visualizations include:</h4>
<ul>
  <li>Hires by technology (pie chart)</li>
  <li>Hires by year (horizontal bar chart)</li>
  <li>Hires by seniority (bar chart)</li>
  <li>Hires by country over years (USA, Brazil, Colombia, and Ecuador only) (multiline chart)</li>
</ul>

<h3>Dataset</h3>

<p>
The initial dataset is synthetic and random, containing 50,000 entries and 11 attributes. Some of the most important columns are:
</p>

<ul>
  <li>YOE -> Years of Experience</li>
  <li>Application Date</li>
  <li>Seniority</li>
  <li>Country</li>
  <li>Technology</li>
  <li>Code Challenge Score</li>
  <li>Technical Interview Score</li>
</ul>

<p>
We are looking to answer fundamental questions, create relevant visualizations, and draw some insightful conclusions based on the data.
</p>

<h2>How to Run</h2>

<ol>
  <li>Create a virtual environment:</li>

  <pre><code>python -m venv venv</code></pre>

  <li>Activate the virtual environment:</li>

  <pre><code>./venv/Scripts/activate</code></pre>

  <li>Install the required libraries:</li>

  <pre><code>pip install -r requirements.txt</code></pre>
  <li>Subsequently, the dataset was uploaded to a PostgreSQL database in its raw form.</li>

  <li>After performing the data cleaning and Exploratory Data Analysis (EDA), the clean dataset was stored back into the PostgreSQL database.</li>

  <li>The connection to the PostgreSQL database was then made from Power BI to create the visualizations.</li>
</ol>

<p><strong>NOTE:</strong> For more details, please refer to the accompanying document.</p>


