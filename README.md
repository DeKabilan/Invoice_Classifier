# Document_Similarity_Matching
 Document Similarity Matching Assignment for Fullstack SWE Intern 2024
 
 <b>Text Extraction:</b>
 <p>The PDF are read through the PyPDF2 library and are converted into a String. The String is next converted to a List with all the words.</p><br>
 
 <b>Similarity Metric - Cosine Similarity:</b>
 <p>By finding the repeated words from the two PDFs using a Hashmap we can calculate the Cosine Similarity using the formula given below,</p><br>
 <img src="./assets/Cosine_Similarity.png"><br>
 <b>Example:</b><br>
 <p>Consider the Table below</p>
 <img src = "./assets/table.png">
 <p>Here the Cosine Similarity can be Calculated by knowing the Repeated Words</p>
 <img src="./assets/example.png"><br>
 <b>Approach:</b>
 <p>To find the Cosine Similarity, I first converted the PDFs to Strings, then the Strings into Lists. Now the counts of each words can be calculated easily using a Hashmaps. Then iterating through all the Keys in the Hashmap we can calculate the Numerator. Similarily the Denominator is also calculated. Therefore the Cosine Similarity is calculated as Numerator/Denominator.</p><br>
 <b>Classification: </b><br>
 <p>To find the similarity, the Cosine Similarity of test PDF to all the PDFs in the Train Directory is computed and the PDF having the largest Cosine Similarity is the most similar to test PDF. Note: In some cases the PDFs don't match and result in a low Similatrity value. So if the Similarity Value is less than 0.2 then the program assumes that there is no match</p>
