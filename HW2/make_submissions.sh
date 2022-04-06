###
 # @Author: Xiang Pan
 # @Date: 2022-02-22 20:21:22
 # @LastEditTime: 2022-03-22 23:49:06
 # @LastEditors: Xiang Pan
 # @Description: 
 # @FilePath: /HW2/make_submissions.sh
 # @email: xiangpan@nyu.edu
### 
rm -r FML-SP22-HW2-xp2030-Xiang-Pan
rm FML-SP22-HW2-xp2030-Xiang-Pan.zip
mkdir FML-SP22-HW2-xp2030-Xiang-Pan
cp -r ./build/main.pdf FML-SP22-HW2-xp2030-Xiang-Pan/FML-SP22-HW2-xp2030-Xiang-Pan.pdf
cp -r main.tex FML-SP22-HW2-xp2030-Xiang-Pan/
cp -r main.bib FML-SP22-HW2-xp2030-Xiang-Pan/
zip -r FML-SP22-HW2-xp2030-Xiang-Pan.zip FML-SP22-HW2-xp2030-Xiang-Pan/