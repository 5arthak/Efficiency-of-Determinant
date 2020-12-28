Sarthak Agarwal
20 June 2019

Efficiency of Determinant Calculation Methods

Abstract: ​For a square matrix, one can capture relevant information by using just a
single number, called the determinant. In mathematics, the concept of determinant comes handy for various purposes like solving linear equations, capturing how linear transformation change the geometry of the system. Studying square matrices is fascinating because of their beautiful and organized symmetry having an equal number of rows and columns. This symmetry enables us to use different methods to manipulate the matrix elements and calculate many essential values, including its determinant. Especially with the extensive use of Linear Algebra and square matrices in the field of computer science, it is imperative to know which of the methods to calculate the determinant is the most efficient way.

Introduction: ​For the completion of this project, I have used python to compute the determinant of the n*n matrix using three different methods:

1. Checking for a Special Matrix.
a. Upper Triangular Matrix
b. Lower Triangular Matrix
c. Diagonal Matrix

2. Gaussian Elimination
3. Calculating the minor of a matrix using recursion.

After computing the determinant of the matrix, I have calculated the time taken it takes for the script to run each algorithm and then we can compare the time taken for the different processes to come to a conclusion on which method is the fastest and the most efficient of all that we have calculated.
Definition of Determinant:​ Determinant of (n x n) a matrix and is a real or a complex number that is associated with many properties that the matrix possesses. One way to define the determinant of a (n x n) matrix ​A​ is the formula:
where the terms are summed over all permutations, and the sign is positive if the permutation is even, and for odd it is negative.
Working of all Algorithms:
1. Checking for a Special Matrix​: Upper Triangular, Lower Triangular, and Diagonal matrices are considered to be unique because of their standout symmetry. This outstanding symmetry provides them with exceptional properties. One of these properties being the ​determinant equal to the product of elements​ that sit on the diagonal of the matrix.
Algorithm:​ After the user selects this option from the menu the python script with check if the entered matrix is diagonal, upper triangular or lower triangular, if the kind of inputted matrix is special, we extract the elements that sit on the diagonal and multiply them to find the determinant.
2
  
 Code:
Checking for LOWER TRIANGULAR MATRIX:
Checking for UPPER TRIANGULAR MATRIX:
Checking for Diagonal Matrix: ​To check if the matrix is a Diagonal MatrixI have check if the inputted matrix is both Upper Triangular and Lower Triangular.
Code for the Main Algorithm:
3
    
 Output​: Output1:
Output 2:
4
  2. ​Determinant by Gaussian Elimination: ​Gaussian Elimination is one of the most important algorithms in the field of both Linear Algebra and Computer Science. The algorithm involves applying simple row transformations rules to a matrix and converting it to the reduced form.
Row Transformation rules involved in the process:
● ● ●
We can multiply any row by any non zero constants. We can switch any two rows.
You can add two rows together.

 Algorithm: ​To calculate the determinant using the Gaussian elimination process, we use the Gaussian elimination rules to convert the given matrix to a lower or upper triangular matrix, and after the model is converted to a particular pattern we extract its diagonal and find the product of diagonal elements.
Code:
5
  Output:
 
 3. ​Calculating Determinant of a matrix using recursion:
● What is recursion?
● Recursion is a process in which a function calls itself directly or indirectly is
called recursion and the corresponding function is called a recursive function.
(Recursion, “GeeksforGeeks.org”)
​Algorithm: ​The technique of calculating the determinant using the ‘Laplacian’
method or the minor expansion method is very famous although the Gaussian Elimination is a more efficient way to calculate the determinant.
In the algorithm that my script uses the recursion technique to find the minor expansion of the matrix and then computing the determinant using the formula:
Where Mij is a so-called ​minor​ of A, obtained by taking the determinant of A with
row i and column j "crossed out." Code:
6
   
 Output:
7
 Comparing Efficiencies:
Efficiency ​of the algorithm is a very important factor that determines which algorithm is the most suitable for using especially when making humungous programs for the industry. Matrices are used in the Computer Science for calculation purposes all the time and therefore it is important to figure out the efficiency of the determinant calculation algorithm efficiency. Analysis:
From the above mentioned three methods:
● Calculating the determinant by checking for a special matrix is a reasonably inefficient process, and the fact that it does not apply to every possible model makes this approach the most inefficient way of calculating the determinant matrix.
● Gaussian Elimination is the most efficient process of calculating the determinant. The easy algorithm and time efficiency together make Gaussian Elimination a very reliable process of finding the determinant.
● From the results in the output, it is reasonably evident that calculating the determinant using recursion and minor expansion is not the most efficient process. On average, the Gaussian elimination is almost six times faster than the recursive process.
  
 Works Cited
Daddel, Ali A. “Definition of Determinant.” ​Definition of Determinant,​ 15 Sept. 2000, www.math.ucdavis.edu/~daddel/linear_algebra_appl/Applications/Determinant/Determinant/n ode3.html.
“Determinant Expansion by Minors.” ​From Wolfram MathWorld​, mathworld.wolfram.com/ DeterminantExpansionbyMinors.html.
“Recursion.” ​GeeksforGeeks,​ 17 Apr. 2019, www.geeksforgeeks.org/recursion/.
8
