# LEXER

Additional resources for understanding tokens, FSMs, the lexer algorithm, and the code provided for this project are provided in the _Lectures: Reading, Topics, and Slides_ section of the _Content_ pane on [learningsuite.byu.edu](https://learningsuite.byu.edu). Look for _FSMs in Project 1_ in the _September Lectures_.  **We strongly recommend that you review that content, including the Jupyter notebook, before proceeding further.**

Perhaps the easiest way to understand the input to output relationship for the lexer is through a few examples.

## Example 1
**Input:**

<pre>
Queries:
   marriedTo ('Bea' , 'Zed')?

Rules:
   marriedTo( X,Y ) :- marriedTo(Y,X) .
</pre>


**Output:**
<pre>
(QUERIES,"Queries",2)
(COLON,":",2)
(ID,"marriedTo",3)
(LEFT_PAREN,"(",3)
(STRING,"'Bea'",3)
(COMMA,",",3)
(STRING,"'Zed'",3)
(RIGHT_PAREN,")",3)
(Q_MARK,"?",3)
(RULES,"Rules",5)
(COLON,":",5)
(ID,"marriedTo",6)
(LEFT_PAREN,"(",6)
(ID,"X",6)
(COMMA,",",6)
(ID,"Y",6)
(RIGHT_PAREN,")",6)
(COLON_DASH,":-",6)
(ID,"marriedTo",6)
(LEFT_PAREN,"(",6)
(ID,"Y",6)
(COMMA,",",6)
(ID,"X",6)
(RIGHT_PAREN,")",6)
(PERIOD,".",6)
(EOF,"",8)
Total Tokens = 26
</pre>

## Example 2
**Input:**
<pre>
,
'a string'
# a comment
Schemes
FactsRules
::-
</pre>

**Output**
<pre>
(COMMA,",",1)
(STRING,"'a string'",2)
(COMMENT,"# a comment",3)
(SCHEMES,"Schemes",4)
(ID,"FactsRules",5)
(COLON,":",6)
(COLON_DASH,":-",6)
(EOF,"",7)
Total Tokens = 8
</pre>

## Formal Specifications of Token Types
The following table describes each token that must be recognized by the lexer

<table>
    <tbody>
        <tr>
            <th>Token Type</th>
            <th>Description</th>
            <th>Examples</th>
        </tr>
        <tr>
            <td class="center">COMMA</td>
            <td class="center">The <span class="code">&#39;,&#39;</span> character</td>
            <td class="center">,</td>
        </tr>
        <tr>
            <td class="center">PERIOD</td>
            <td class="center">The <span class="code">&#39;.&#39;</span> character</td>
            <td class="center">.</td>
        </tr>
        <tr>
            <td class="center">Q_MARK</td>
            <td class="center">The <span class="code">&#39;?&#39;</span> character</td>
            <td class="center">?</td>
        </tr>
        <tr>
            <td class="center">LEFT_PAREN</td>
            <td class="center">The <span class="code">&#39;(&#39;</span> character</td>
            <td class="center">(</td>
        </tr>
        <tr>
            <td class="center">RIGHT_PAREN</td>
            <td class="center">The <span class="code">&#39;)&#39;</span> character</td>
            <td class="center">)</td>
        </tr>
        <tr>
            <td class="center">COLON</td>
            <td class="center">The <span class="code">&#39;:&#39;</span> character</td>
            <td class="center">:</td>
        </tr>
        <tr>
            <td class="center">COLON_DASH</td>
            <td class="center">The string <span class="code">&quot;:-&quot;</span></td>
            <td class="center">:-</td>
        </tr>
        <tr>
            <td class="center">SCHEMES</td>
            <td class="center">The string <span class="code">&quot;Schemes&quot;</span></td>
            <td class="center">Schemes</td>
        </tr>
        <tr>
            <td class="center">FACTS</td>
            <td class="center">The string <span class="code">&quot;Facts&quot;</span></td>
            <td class="center">Facts</td>
        </tr>
        <tr>
            <td class="center">RULES</td>
            <td class="center">The string <span class="code">&quot;Rules&quot;</span></td>
            <td class="center">Rules</td>
        </tr>
        <tr>
            <td class="center">QUERIES</td>
            <td class="center">The string <span class="code">&quot;Queries&quot;</span></td>
            <td class="center">Queries</td>
        </tr>
        <tr>
            <td class="center">WHITESPACE</td>
            <td class="center">Sequence of &quot; &quot;, &quot;\t&quot;, &quot;\n&quot;, or &quot;\r&quot;</td>
            <td class="center">A sequence&nbsp;of adjacent white space characters</td>
        </tr>
        <tr>
            <td class="center">ID</td>
            <td class="widthLimit">An identifier is a letter followed by zero or more letters or digits, and is not a keyword (Schemes, Facts, Rules, Queries).<br />
            Note that for the input &quot;1stPerson&quot; the lexer would find two tokens: an &#39;undefined&#39; token made from the character &quot;1&quot; and an &#39;identifier&#39; token made from the characters &quot;stPerson&quot;.</td>
            <td class="center">
            <table>
                <tbody>
                    <tr>
                        <th>Valid Identifiers</th>
                        <th>Invalid Identifiers</th>
                    </tr>
                    <tr>
                        <td>Identifier1</td>
                        <td>1stPerson</td>
                    </tr>
                    <tr>
                        <td>Person</td>
                        <td>Schemes</td>
                    </tr>
                </tbody>
            </table>
            </td>
        </tr>
        <tr>
            <td class="center">STRING</td>
            <td class="widthLimit">
            <p>A string is a sequence of characters enclosed in single quotes. White space (space, tab, etc.) is not skipped when inside a string. Two adjacent single quotes within a string denote an apostrophe. The line number for a string token is the line where the string begins. If a string is not terminated (end of file is encountered before the end of the string), the token becomes an undefined token.<br />
            <br />
            The &#39;value&#39; of a token printed to the output is the sequence of input characters that form the token. For a string token this means that two adjacent single quotes in the input are printed as two adjacent single quotes in the output. (In other words, don&#39;t convert two adjacent single quotes in a string to just one apostrophe in the output.)</p>
            </td>
            <td class="center"><span class="code">&#39;This is a string&#39;</span><br />
            <br />
            <span class="code">&#39;&#39;</span> -- (The empty string)<br />
            <br />
            <span class="code">&#39;This isn&#39;&#39;t two strings&#39;</span><br />
            &nbsp;</td>
        </tr>
        <tr>
            <td class="center" rowspan="2">COMMENT</td>
            <td>A comment starts with a hash character (#) and ends at the end of the line or end of the file.</td>
            <td class="center"><span class="code"># This is a comment </span></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="center">&nbsp;</td>
        </tr>
        <tr>
            <td class="center">UNDEFINED</td>
            <td class="widthLimit">Any character not tokenized as a string, keyword, identifier, symbol, or white space is undefined. Additionally, any non-terminating string is undefined. In that case, you reach EOF before finding the end of the string. Any undefined token should result in the creation of&nbsp;<strong>one&nbsp;</strong>undefined token (this will always be the last token you create). The program should then end execution by returning the current list of tokens.&nbsp;</td>
            <td class="center"><span class="code">$&amp;^ (Three undefined tokens)</span><br />
            <br />
            <span class="code">&#39;a string that does not end</span><br />
            &nbsp;</td>
        </tr>
        <tr>
            <td class="center">EOF</td>
            <td class="center">The end of the input file.</td>
            <td class="center">&nbsp;</td>
        </tr>
    </tbody>
</table>

## Lexer Algorithm

This overview is very high-level. The `lexer` function in `src/project1/lexer.py` has detailed pseudo-code that can be helpful as well.
The following diagram is an illustration of the what takes place during lexing. The input is given to each of the token FSMs, and the one that reads the most characters and has the highest priority in the case of a tie yields the token for that portion of the input. The list of tokens is in the upper right of the diagram. The list of machines in the center. And the input, with the already processed input crossed out, is in the left of the diagram.

<p align="center">
<img src="../images/project1_diagram.jpg" alt="drawing" width="800"/>
</p>

The general pseudo-code follows. The code gives the input to each of the state machines and keeps track of the machine that reads the most input characters with the resulting token. In the case of a tie, the machine that appears first in the array of FSMs has priority. Missing from the code is how an `UNDEFINED` token should be handled and `WHITESPACE`. For `UNDEFINED`, if no machine matches, then return `UNDEFINED` with the first character af the input as the value. For `WHITESPACE` it is it's own FSM, so it will match when it can, and create a `WHITESPACE` token that is to be ignored.

<p align="center">
<img src="../images/pseudo-code.jpg" alt="drawing" width="800"/>
</p>

With the above, the general algorithm for the lexer is understood as follows:

* While there are characters in string left to process
    * Run each FSM on the string
    * Choose the “winning” FSM
    * Add the corresponding token to a list
    * Advance to next part of input_string
