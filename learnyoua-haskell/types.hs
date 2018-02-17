removeNonUpper :: String -> String
removeNonUpper st = [c | c <- st, c `elem` ['A'..'Z']]

-- type annotation
five = read "5" :: Int