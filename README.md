# datlib
This is a python package containing useful classes and functions of data structures and algorithms.

## Installation

Run the following to install:

'''python

   pip install datlib
   
'''
## Usage

There are many modules inside this package.

###1. rangeQueries module

      This module contains a class name SegmentTree.
      The constructor of the class takes following arguments :

      (a) A function **combine**
          This takes two arguments a and b. This function takes care of 
          the combination of the values of child nodes into a parent node.
        

      (b) A variable **identityVal**
          
          An identity value for filling the empty nodes in the segment tree
          array and for the case when the query is completely outside the 
          range.

      (c) A list **l**

          This contains the list for which you have to make the SegmentTree.

      You can make the segment tree in following way : 

      '''python
         
         from rangeQueries import SegmentTree
         def combine(a,b):
             return a+b
                 
         s = SegmentTree(l,identityVal,combine)

      '''

      You can call following methods on your segment tree :
      
      (a) query(qs,qe)
          
          This method will take two parameters qs and qe. And will perform 
          query for the range.

      (b) pointUpdate(val,qi)
          
          This method will take two parameters qi and val,where qi is the 
          index of the given list **l** on which we will update the value
          to **val**.This will update the your segment tree.

      (c) rangeUpdate(qs,qe,val)

          This method will take three parameters qs,qe and val.This method
          will update the values to **val** from index **qs** to **qe**.
          This will update the your segment tree.

###2. numbertheory module
      
      This module contains following functions :
    
      (a) primefactors(n)

          This function will return all the prime factors of a number.

      (b) chkPrime(n)
     
          This function will check if a number is prime or not.

      (c) divisors(n)
          
          This function will return all the divisors of a number.
      
      (d) powerModulo(x,y,M)

          This function will calculate x^y modulo M.


###3. graphs module

      This module contains following functions :
      Here **n** is the number.
    
      (a)  bfs(start,graph)

           This function will take two arguments start and graph.
           Start is the source node which can be a tuple,number or a string.
           graph is a dictionary which contains the adjacency list of the nodes.
           This function will return a dictionary containing distance of all the
           nodes from the source node.

      (b) dfs(start, graph)
     
          This function will take two arguments start and graph.
          Start is the source node which can be a tuple,number or a string.
          graph is a dictionary which contains the adjacency list of the nodes.
          This function will contain a set of all the nodes that can be reched
          from start.
                             
