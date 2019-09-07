3行代码实现gif裁切

最近在做动态二维码的时候碰到一个问题，从网上下载的动态gif不是正方形的，很难看，本来想找个软件来处理的，竟然没找到，只好自己动手。

先来看效果：


代码的确只有三行：
第一行：读取gif图片。
第二行：分解gif图片帧并进行裁切。
第三行：按照原gif的参数组装新的gif。

代码如下（需要用到PIL库）：

```python
def crop_gif_short(gif, gif_out, box):
    im = Image.open(gif)
    frames = [im.crop(box) for frame in range(0, im.n_frames) if not im.seek(frame)]
    frames[0].save(gif_out, save_all=True, append_images=frames, loop=0, duration=im.info['duration'])
```

可读性更高一点的版本：
```python
def crop_gif(gif, box):
    """
    Crop gif picture.
    Args:
        gif: gif file name
        box: crop box (left, up, right, down)
    """
    _, file = os.path.split(gif)
    name, ext = os.path.splitext(file)

    im = Image.open(gif)
    frames = []
    for frame in range(0, im.n_frames):
        im.seek(frame)
        frames.append(im.crop(box))
    frames[0].save(name + '_crop' + ext,
                   save_all=True,
                   append_images=frames,
                   loop=0,
                   duration=im.info['duration'])
```

另外，生成动态二维码也只需要一行代码，如下（需要用到myqr库）：
```
myqr.run( words = get_text(origin),
              version = 1,
              level = 'H',
              picture = picture,
              colorized = True,
              contrast = 2.0,
              brightness = 1.0,
              save_name = save_name,
              save_dir = path)
```
其中words是二维码内容，picture是背景图，save_name是保存名称，save_dir是保存路径。

二维码内容可以通过pyzbar库进行读取，代码如下（需要用到pyzbar库）：
```
def get_text(f):
    return ''.join([_.data.decode('utf-8') for _ in pyzbar.decode(Image.open(f))])
```

生成的动态二维码效果如下：

