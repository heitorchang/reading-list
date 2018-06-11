-- ch01/wc.hs
-- http://book.realworldhaskell.org/read/getting-started.html
-- counts number of lines in its input

main = interact wordCount
     where wordCount input = show (length (lines input)) ++ "\n"