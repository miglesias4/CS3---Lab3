# -*- coding: utf-8 -*-
"""
Created and modified by: Matthew Iglesias
80591632
Diego Aguirre 
T.A. Anitha Nath
"""
from AVLtree import AVLTree, Node
from RedBlackTree import RedBlackTree, RBTNode

def user_tree(user_input):
    if user_input is "A" or "RB":
        if user_input is "A":
            print("Generating tree...") 
            english_words = AVLTree()
            with open("words.txt") as f:
                for avl_line in f:
                    english_words.insert(Node(avl_line.rstrip('\n'))) ##Appends into AVL tree
            return english_words
            
        elif user_input is "RB":
            print("Generating tree...") 
            english_words = RedBlackTree()
            with open("words.txt") as m:
                for rb_line in m:
                    english_words.insert(RBTNode(rb_line.rstrip('\n'))) ##Appends into RB tree
            return english_words
        else:        
            print("Invalid Argument")
            return None
        return english_words
    
def print_anagrams(word,english_words,prefix =""):
    if len(word) <= 1:
        str = prefix + word
        #print(str, english_words.search(str))
        if english_words.search(str):
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] ##letters before cur
            after = word[i + 1:] ##letters after cur
            if cur not in before:
                print_anagrams(before + after,english_words,prefix + cur)
                
def count_anagrams(word,english_words,prefix =""):
    count = 0
    if len(word) <= 1:
        str = prefix + word
        if english_words.search(str):
            count += 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] ##letters before cur
            after = word[i + 1:] ##letters after cur
            if cur not in before:
                count += count_anagrams(before + after,english_words,prefix + cur)
    return count

def main():
    ##Asks user if they want AVL or Red and Black Tree
    user_desired = input("Choose AVL Tree(A) or Red and Black Tree(RB): ")
    english_words = user_tree(user_desired)
    print("Your choice word is: ",english_words.search("spot"))
    print_anagrams("spot", english_words) ##Prints the anagrams associated with the word
    print("Number of anagrams asscciated: ",count_anagrams("spot",english_words)) ##Prints the number of anagrams from word
    
main()