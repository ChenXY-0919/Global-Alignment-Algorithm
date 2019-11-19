Global-Alignment-Algorithm
==================================================================================
Global Alignment Algorithm(`Needleman and Wunsch,1970`) based on python  
  
Usage
----------------------
Linux bash shell or windows cmd:  

* Switch the working path to the folder where the program is located.  
  * get usage:
```Bash
python bin/scratch.py -h  
optional arguments:  
  -h, --help            show this help message and exit  
  -v, --copyright       The information of version and author  
  -s SCORING_MATRIX, --scoring_matrix SCORING_MATRIX  
                        The path of scoring matrix for alignment  
  -f FILE, --file FILE  The path of file of sequence in FASTA  
  -o OUTPUT, --output OUTPUT  
                        Specify output path for result, Default:output on  
                        screen  
  -q, --quiet           without status prompt  
  -g GAP, --gap GAP     Input the gap panel, Default:-5.  
  -a SEQ1, --seq1 SEQ1  Input the sequence1 directly without option '-f'  
  -A SEQ2, --seq2 SEQ2  Input the sequence2 directly without option '-f'  
  -m MAX_OUTPUT, --max_output MAX_OUTPUT  
                        Set the max number of alignment results to  
                        output.,Default:100  
 ```
  Eg. 1  
  ```Bash
  python bin/scratch.py -s test_data/scoring_matrix.txt -f test_data/ACTB.txt -o result.txt
  ```
  Eg.2  
  ```Bash
  python bin/scratch.py -s test_data/scoring_matrix.txt -A AGC -a AAG
  ```
