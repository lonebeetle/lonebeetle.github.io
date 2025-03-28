---
title: "My First Post"
date: 2025-03-27T23:46:57+08:00
categories:
  - experiment
tags:
  - 博客搭建
---

## 不知道写啥

这是我的另外一次尝试。

行内数学公式：$a^2 + b^2 = c^2$。

块公式，

$$
a^2 + b^2 = c^2
$$

<div>
$$
\boldsymbol{x}_{i+1}+\boldsymbol{x}_{i+2}=\boldsymbol{x}_{i+3}
$$
</div>


```css
.postfdssf {
  color: red;
  font-weight: bold;
}
```

```c++
#include <iostream>
#include "Sales_item.h"
int main()
{
    Sales_item total; // variable to hold data for the next transaction
    // read the first transaction and ensure that there are data to process
    if (std::cin >> total)
    {
        Sales_item trans; // variable to hold the running sum
        // read and process the remaining transactions
        while (std::cin >> trans)
        {
            // if we’re still processing the same book
            if (total.isbn() == trans.isbn())
                total += trans; // update the running total
            else
            {
                // print results for the previous book
                std::cout << total << std::endl;
                total = trans; // total now refers to the next book
            }
        }
        std::cout << total << std::endl; // print the last transaction
    }
    else
    {
        // no input! warn the user
        std::cerr << "No data?!" << std::endl;
        return -1; // indicate failure
    }
    return 0;
}

/* input:
0-201-70353-X 4 24.99
0-201-82470-1 4 45.39
0-201-88954-4 2 15.00
0-201-88954-4 5 12.00
0-201-88954-4 7 12.00
0-201-88954-4 2 12.00
0-399-82477-1 2 45.39
0-399-82477-1 3 45.39
0-201-78345-X 3 20.00
0-201-78345-X 2 25.00
*/
```
+++
title = '使用 warp 来解除 imgur 的访问限制'
date = 2024-10-25T07:39:09+08:00
categories = []
tags = ["Bilibili", "小寄巧"]
+++

或许也可以让 chatgpt 的访问更加丝滑。

起因是在看 react 的官方教程时，发现有一张图片无法访问，对，就是下面这张，

![](https://i.imgur.com/yXOvdOSs.jpg)

其实我最近两年的 imgur 的访问一直比较有问题，有时候需要换很多个节点才能尝试出来一个可以正常加载 imgur 图片的 ip，而有时候甚至会全军覆没。

今天实在忍不了了，所以，就在网上找了一下有没有好的方法可以实现 imgur 的图片的正常访问，因为这个图床(图片托管网站)用到的地方挺多的，比如，像上面的 reactjs 的官网都会用到，还有 v 站也是默认会渲染 imgur 的图片，我自己的博客之前也是用 imgur 比较多，现在则换成了访问更加顺畅的 postimage，不过，我还有很多图片没有迁移过去，所以，解决 imgur 这个图床的问题迫在眉睫。找了一圈，发现还是用 warp 套一层比较合适。

那么，具体是怎么操作呢？

经过我的尝试，发现使用第三方开源的 [cli](https://github.com/ViRb3/wgcf) 而非是 cloudflare 的官方 cli 在 Arch 上的体验是更加丝滑的，具体可以参考 Reddit 的这个帖子，

<https://www.reddit.com/r/CloudFlare/comments/q0hqj4/warpcli_is_not_working/>

具体来讲，就是先安装几个依赖，

```shell
yay -S cloudflare-warp-bin wireguard-dkms openresolv wireguard-tools wgcf
```

这里在安装完毕之后，不要忘记 reboot 一下。

然后，来到一个临时的目录，依次执行，

```shell
wgcf register
wgcf generate
cp ./wgcf-profile.conf /etc/wireguard/
```

然后，

```shell
wg-quick up wgcf-profile
```

然后，就可以查看一下 warp 的状态了，

```shell
curl https://www.cloudflare.com/cdn-cgi/trace/
```

我这里的输出为，

```txt
fl=412f42
h=www.cloudflare.com
ip=2a09:bac5:55fd:1028::19c:2a
ts=1729814011.542
visit_scheme=https
uag=curl/8.10.1
colo=SIN
sliver=none
http=http/2
loc=SG
tls=TLSv1.3
sni=plaintext
warp=on
gateway=off
rbi=off
kex=X25519
```

可以看到，warp 已经 on 的状态了。

如果想要关闭，那么，这个时候，就可以 down 一下，

```shell
wg-quick down wgcf-profile
```

这样一来，imgur 对 ip 的限制就被我们绕过去了。

比如，我以前很多博客的封面都是存在在 imgur 的，那么，我们可以看一下，访问的效果如何，

<https://fanlumaster.github.io/page/4/#board>


