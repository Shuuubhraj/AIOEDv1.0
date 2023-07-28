<h1>AIOED: ALL in One Encryption Decryption</h1>

<p align="left">
  <img alt="Python Version" src="https://img.shields.io/badge/Python-3.x-blue.svg">
</p>


<p><strong>AIOED</strong> (All in One Encryption Decryption) is a Python command-line tool that provides interactive encryption and decryption functionalities using various encryption algorithms, including <strong>DES, AES, and 3DES.</strong> With this tool, you can encrypt sensitive information and decrypt it when needed, all from the comfort of your terminal.</p>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>pycryptodome</code> library (install using <code>pip install pycryptodome</code></li>
</ul>

<h2>Usage</h2>
<ol>
  <li>Clone this repository or download the <code>aioed.py</code> script directly.</li>
  <li>Ensure you have Python 3.x and the required <code>pycryptodome</code> library installed.</li>
  <li>Open a terminal or command prompt and navigate to the directory where <code>aioed.py</code> is located.</li>
  <li>Run the script using the command <code>python aioed.py</code>.</li>
</ol>

<h2>Supported Encryption Algorithms</h2>
<h3>AES (Advanced Encryption Standard)</h3>
<ul>
  <li>Key Length Size: 16 bytes (128-bit), 24 bytes (192-bit), or 32 bytes (256-bit)</li>
  <li>Maximum Plaintext Size: Determined by the key length and padding scheme</li>
</ul>

<h3>DES (Data Encryption Standard)</h3>
<ul>
  <li>Key Length Size: 8 bytes (64-bit)</li>
  <li>Maximum Plaintext Size: 8 bytes</li>
</ul>

<h3>3DES (Triple Data Encryption Standard)</h3>
<ul>
  <li>Key Length Size: 16 bytes (128-bit) or 24 bytes (192-bit)</li>
  <li>Maximum Plaintext Size: 8 bytes</li>
</ul>

<h2>Usage in Education</h2>
<p><strong>AIOED</strong> can serve as a valuable educational tool for universities, colleges, and schools to teach students about encryption techniques and their implementations. It can be used to demonstrate the principles of encryption, decryption, and the importance of secure communication in various information security courses.</p>

<h2>Disclaimer</h2>
<p><strong>AIOED</strong> is intended for educational and experimental purposes only. While the encryption algorithms used are well-known, this tool may not provide the level of security required for sensitive or production use cases. The user is responsible for understanding the security implications of using this tool. Use at your own risk.</p>

<h2>Author</h2>
<p><strong>Rajput Shubhraj Singh</strong></p>
<ul>
  <li>GitHub: <a href="https://github.com/shuuubhraj">shuuubhraj</a></li>
</ul>

<h2>Acknowledgments</h2>
<p>The implementation of encryption and decryption algorithms in this tool is made possible by the <code>pycryptodome</code> library. I acknowledge the contributions of the library's developers and the broader open-source community, which make projects like <strong>AIOED</strong> possible.</p>
