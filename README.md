<h1>DebugBar Checker</h1>

<p>This Python script is a simple tool that checks for the presence of various debuggers in a list of URLs. It uses Python's <code>requests</code> library to make HTTP requests and checks for specific debugger strings in the response content.</p>

<h2>Requirements</h2>

<p>Before running the script, ensure you have the following requirements installed:</p>

<h3><code>requirements.txt</code></h3>

<pre>
colorama
requests
</pre>

<p>You can install the requirements using the following command:</p>

<pre>
pip install -r requirements.txt
</pre>

<h2>How to Use</h2>

<ol>
  <li>Prepare a file <code>list.txt</code> containing a list of URLs, one URL per line.</li>
  <li>Run the script and provide the <code>list.txt</code> file as input.</li>
</ol>

<pre>
python scan.py
</pre>

<p>The script will then check each URL for the presence of different debuggers and print the results to the console. It will also save the URLs with debuggers found in separate result files.</p>
<p>Before running the script, make sure to replace the contents of <code>list.txt</code> with the URLs you want to check for debuggers.</p>
<br>
<p><em><strong>Important Note</strong>: Use this tool responsibly and only on websites you own or have explicit permission to test. Unauthorized testing of websites is against the law and could lead to legal consequences. Always respect the privacy and security of others.</p></em>
