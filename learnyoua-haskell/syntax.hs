capital :: String -> String
capital "" = "Empty String, whoops!"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

bmiTell :: (RealFloat a) => a -> String
bmiTell bmi
        | bmi <= 18.5 = "underweight"
        | bmi <= 25.0 = "normal"
        | bmi <= 30.0 = "overweight"
        | otherwise = "obese"  -- otherwise is a keyword equal to True