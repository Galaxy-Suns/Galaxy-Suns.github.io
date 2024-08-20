# *捌*_项目前置知识
 
* [8.1_网站和网页的关系](#8.1_网站和网页的关系)
* [8.2_骨架标签](#8.2_骨架标签)
* [8.3_SEO三大标签](#8.3_SEO三大标签)
* [8.4_`favicon`_标题图标](#8.4_`favicon`_标题图标)

---

## 8.1_网站和网页的关系

*网站包含多个网页*

*每个网页是一个独立的界面，包含在同一个网站中*

*多个同主题的网页组合在一起，成为一个网站*

## 8.2_骨架标签

* `<!DOCTYPE html>` 文档类型声明，告诉所有浏览器该网页的HTML版本以解析页面，这里的版本`html`是html5
* `<html lang="en">` 语言:英文 `zh-CN`简体中文 `en` 英文
* `<meta charset="UTF-8">` 规定网页的字符编码 `UTF-8` 万国码-容纳了被认证的所有国家的语言 **常用**`GBK2312` 6000+汉字 `GBK` 20000+汉字
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">` 宽度和设备宽度相等-移动端网页需要

## 8.3_SEO三大标签

**什么是SEO**

搜索引擎优化(SEO),可以让网站在搜索引擎上排名靠前

**SEO方法**

* 竞价排名
* 将网页制作为`.html`后缀
* **标签语义化:在合适的地方使用合适的标签**

**SEO三大标签**

* `title` 网页标题双标签
* `description` 网页描述标签 <br> 实为`meta`单标签，`name`属性为`description`,内容写在`content属性` <br> **Emmet** meta:desc
* `keywords` 网页关键词标签 <br> 实为`meta`单标签，`name`属性为`keywords`,内容写在`content属性` <br> **Emmet** meta:kw

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- meta:desc -->
    <meta name="description" content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。">
    <!-- meta:kw -->
    <meta name="keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东">
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title> 
    <link rel="stylesheet" href="./try.css">   
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

## 8.4_`favicon`_标题图标

*标题旁的小图*

*需要.ico格式的图标放在根目录(和html文件同级)*

**语法**

* `<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">`
* **Emmet** `link:favicon`
* .ico图标要命名`favicon.ico`

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- meta:desc -->
    <meta name="description" content="京东JD.COM-专业的综合网上购物商城，为您提供正品低价的购物选择、优质便捷的服务体验。商品来自全球数十万品牌商家，囊括家电、手机、电脑、服装、居家、母婴、美妆、个护、食品、生鲜等丰富品类，满足各种购物需求。">
    <!-- meta:kw -->
    <meta name="keywords" content="网上购物,网上商城,家电,手机,电脑,服装,居家,母婴,美妆,个护,食品,生鲜,京东">
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title> 
    <link rel="stylesheet" href="./try.css">  
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon"> 
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

