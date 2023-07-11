# sd-webui-easy-prompt-selector-zh_CN

## 增加新功能提示图
![tagImg](https://github.com/n714/sd-webui-easy-prompt-selector-zh_CN/assets/45053630/490b6f3e-c940-4254-b8b4-214fb0ef52ea)
- 当鼠标悬停于提示词上，下方将会显示显示有关图像。

[Video](https://github.com/n714/sd-webui-easy-prompt-selector-zh_CN/assets/45053630/67102b31-84b2-49fa-8dc7-e3cb0d86b552)

- 新增提示词库和新疆图像安装如下：
-举例说明：
-人物提示词加上图表示，
-在tag档案夹内新增档案夹新建 人物 / 角色(Characters),把图片放进档案夹里,图片名称须根描述词一致.
-如果图像党不是JPG格式，需要加上下面两句，如果是JPG格式的话不需要加。
-以这个例子为例,我上床了六个图片分别改名为:
- 1个女孩.png
-  1个男孩.png
-  2个女性.png
-  多个女孩.png
-  老太太.png
-  老人.png
  
```
# 如果图像党不是JPG格式，需要加上下面两句
.settings:
 fileFormatForImages: png

人物:
 角色(Characters):
  1个女孩: 1girl
  1个男孩: 1boy
  2个女性: 2girls
  多个女孩: multiple girls
  老太太: Old lady
  老人: Old man 
```
 
## 如何安装 stable diffusion webui easy prompt selector zh_CN 简体中文

  ### 1.通过网址安装
  
  - 点击 `Extension` 选项卡，点击 `Install from URL` 子选项卡
  - 复制本 git 仓库网址：
  ```
https://github.com/n714/sd-webui-easy-prompt-selector-zh_CN
  ```
![2](https://github.com/n714/sd-webui-easy-prompt-selector-zh_CN/assets/45053630/bbd0f896-3d9b-4b93-b76f-6fd1422c758c)
 
  - 粘贴进 URL 栏，点击 `Install`，如图
  - 安装完成，  

  ### 2. 又或者，直接下载然后放在对应路径
  [下载本 git 仓库](https://github.com/n714/sd-web-easy-prompt-selector-cn/archive/refs/heads/main.zip) 为 zip 档案
```
git clone https://github.com/n714/sd-webui-easy-prompt-selector-zh_CN
  ```

  - 解压，并把文件夹放置在 webui 根目录下的 `extensions` 文件夹中，放好之后, 重新webui.
  - 安装完成.

  ## 安装提示词库
- [简体中文提示词库](https://github.com/n714/stable-diffusion-prompt-library-zh_CN)
- [繁體中文提示詞庫](https://github.com/n714/stable-diffusion-prompt-library-zh_TW)

### 提示词库内容
- 0 - 起手提示词 
- 0 - 负面提示词 
- 1 - 人物 
  
下载然后放在对应路径
- [Prompt libaray ](https://github.com/n714/stable-diffusion-prompt-library-zh_CN)
- 直接下载然后,解压，并把文件夹放置在 webui 根目录下的 `extensions/sd-webui-easy-prompt-selector-zh_CN/tags/` 文件夹中，
- 安装完成.

------------------------------------------------------------------------------------------
## Original creator
[Original creator instructions](https://blue-pen5805.fanbox.cc/posts/5306601)
