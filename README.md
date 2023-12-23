# Split-vertically-PDF

### コード解説

見開きのPDFを縦に分割して片開きにします。

以下で入力ファイル（分割したいファイル）と分割した後の出力ファイル名を指定します。
```Python
input_file = "かなでるからだ.pdf"  
output_file = "かなでるからだ_split.pdf"  
```

以下は分割位置の調整で、PDFスキャンなどで見開きの中心がずれているときに値を変更することで分割位置を調整できます。中央の時は0.5で(0,1)の任意の値で設定できます。
```Python
    p1_lower_left  = (x0, y0)
    p1_upper_right = (x1 - 0.47 * (x1 - x0), y1)
    p2_lower_left  = (x1 - 0.47 * (x1 - x0), y0)
    p2_upper_right = (x1, y1)
```
