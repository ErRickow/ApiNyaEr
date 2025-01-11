

---

# 📘 API Documentation

Welcome to the **ErApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.

## Installation
To get started, make sure you have the library installed:
```bash
pip3 install ApiNyaEr
```

## Usage
- **Synchronous usage**: Import the library with:
```python
from ApiNyaEr.sync import apinya
```
- **Asynchronous usage**: Import the library with:
```python
from ApiNyaEr import apinya
```

Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀

## Status

| Function           | Status |
|--------------------|--------|
| [1. Ai](#1-ai) | ❌
| [2. Bing Image](#2-bing-image) | ✅
| [3. Blackbox](#3-blackbox) | ✅
| [4. Carbon](#4-carbon) | ✅
| [5. Cat](#5-cat) | ✅
| [6. Dare](#6-dare) | ✅
| [7. Doa](#7-doa) | ❌
| [8. Dog](#8-dog) | ✅
| [9. Fakta Unik](#9-fakta-unik) | ✅
| [10. Gemini](#10-gemini) | ✅
| [11. Get Pinter Url](#11-get-pinter-url) | ❌
| [12. Github Search](#12-github-search) | ✅
| [13. Hug](#13-hug) | ✅
| [14. Kapan Libur](#14-kapan-libur) | ❌
| [15. Luminai](#15-luminai) | ✅
| [16. Nama Epep](#16-nama-epep) | ✅
| [17. Password](#17-password) | ✅
| [18. Pypi](#18-pypi) | ❌
| [19. Qanime](#19-qanime) | ✅
| [20. Qhacker](#20-qhacker) | ✅
| [21. Qislam](#21-qislam) | ✅
| [22. Qpubg](#22-qpubg) | ✅
| [23. Truth](#23-truth) | ✅
| [24. Wibu](#24-wibu) | ✅


## 🎓 How to Use Each Function

### 1. Ai

**Description**:
Interaksi dengan AI Basis Text.

**Args:**
**Description**:
tanya (str): Text inputnya.

**Returns:**
**Description**:
str: Respon chatbotnya.

```python
from ApiNyaEr import apinya

result = await apinya.ai(tanya='Tidur')
print(result)
```

#### Expected Output

```text
Expecting value: line 1 column 1 (char 0)
```

### 2. Bing Image

**Description**:
Cari bing images based om teks.

**Args:**
  - **teks (str)**: Teks quesy yang ingin di cari gambarnya.
  - **limit (int, optional)**: Maximum number photonya. Defaults nya 1.

**Returns:**
  - **list**: List image url yang di terima.

```python
from ApiNyaEr import apinya

result = await apinya.bing_image(teks='Tidur', limit=1)
print(result)
```

#### Expected Output

```text
https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/14044059/Kenali-Pola-Tidur-yang-Baik-untuk-Kesehatan.jpg.webp
```

### 3. Blackbox

**Description**:
Berinteraksi dengan Blackbox AI untuk menghasilkan konten. 🧠

**Args:**
  - **tanya (str)**: Teks masukan untuk berinteraksi dengan API obrolan Blackbox AI.

**Returns:**
  - **requests.Response**: Objek respons dari permintaan API.

```python
from ApiNyaEr import apinya

result = await apinya.blackbox(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "results": "<!DOCTYPE html><html lang=\"en\"><head><meta charSet=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/><link rel=\"preload\" href=\"/_next/static/media/a34f9d1faa5f3315-s.p.woff2\" as=\"font\" crossorigin=\"\" type=\"font/woff2\"/><link rel=\"preload\" href=\"/_next/static/media/bb3ef058b751a6ad-s.p.woff2\" as=\"font\" crossorigin=\"\" type=\"font/woff2\"/><link rel=\"stylesheet\" href=\"/_next/static/css/df842cdd5139c39e.css\" data-precedence=\"next\"/><link rel=\"preload\" as=\"script\" fetchPriority=\"low\" href=\"/_next/static/chunks/webpack-e8afe3ae2f1a0a14.js\"/><script src=\"/_next/static/chunks/fbba8177-539bc59dbe1c191e.js\" async=\"\"></script><script src=\"/_next/static/chunks/4990-86deda367dde3b5b.js\" async=\"\"></script><script src=\"/_next/static/chunks/main-app-08e24d760cf68077.js\" async=\"\"></script><script src=\"/_next/static/chunks/3f9dfec0-695648b36cb4c167.js\" async=\"\"></script><script src=\"/_next/static/chunks/5153-58ea3da6f0a31254.js\" async=\"\"></script><script src=\"/_next/static/chunks/3447-bd02a654a85949f7.js\" async=\"\"></script><script src=\"/_next/static/chunks/5864-cc364f2dfdce9d21.js\" async=\"\"></script><script src=\"/_next/static/chunks/6272-e3b5ade80a66c056.js\" async=\"\"></script><script src=\"/_next/static/chunks/4836-953da52b268fd9a5.js\" async=\"\"></script><script src=\"/_next/static/chunks/7968-4c3079258bc08265.js\" async=\"\"></script><script src=\"/_next/static/chunks/app/layout-b3c5f4a3dd59966c.js\" async=\"\"></script><link rel=\"preload\" href=\"/_next/static/css/42c27cb71e996d58.css\" as=\"style\"/><title>Chat Blackbox: AI Code Generation, Code Chat, Code Search</title><meta name=\"description\" content=\"BLACKBOX AI is the Best AI Model for Code. Millions of developers use Blackbox Code Chat to answer coding questions and assist them while writing code faster. Whether you are fixing a bug, building a new feature or refactoring your code, ask BLACKBOX to help.\n\nBLACKBOX has real-time knowledge of the world, making it able to answer questions about recent events, technological breakthroughs, product releases, API documentations &amp; more\n\nBLACKBOX integrates directly with VSCode to automatically suggests the next lines of code based on your repo context.\"/><meta name=\"keywords\" content=\"blackbox, blackboxai,ai,chat,autocomplete,bash,c,c#,c++,code-recommendation,cpp,csharp,css,domination,go,golang,haskell,html,intellicode,intellisense,java,javascript,julia,jupyter,keybindings,kite,kotlin,lua,method&amp;#32;completion,node,node.js,nodejs,objectivec,objective-c,ocaml,perl,php,python,react,ruby,rust,snippets,swift,typescript\"/><meta property=\"og:image:type\" content=\"image/png\"/><meta property=\"og:image:width\" content=\"1686\"/><meta property=\"og:image:height\" content=\"882\"/><meta property=\"og:image\" content=\"https://https/www.blackbox.ai/opengraph-image.png?49c2c3ea917a06c7\"/><meta name=\"twitter:card\" content=\"summary_large_image\"/><meta name=\"twitter:image:type\" content=\"image/png\"/><meta name=\"twitter:image:width\" content=\"1686\"/><meta name=\"twitter:image:height\" content=\"882\"/><meta name=\"twitter:image\" content=\"https://https/www.blackbox.ai/twitter-image.png?49c2c3ea917a06c7\"/><link rel=\"shortcut icon\" href=\"/favicon-16x16.png\"/><link rel=\"icon\" href=\"/favicon.ico\"/><link rel=\"apple-touch-icon\" href=\"/apple-touch-icon.png\"/><meta name=\"next-size-adjust\"/><script src=\"/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js\" noModule=\"\"></script></head><body class=\"font-sans antialiased custom-scrollbar __variable_d65c78 __variable_3c557b\"><div style=\"position:fixed;z-index:9999;top:16px;left:16px;right:16px;bottom:16px;pointer-events:none\"></div><script>!function(){try{var d=document.documentElement,c=d.classList;c.remove('light','dark');var e=localStorage.getItem('theme');if('system'===e||(!e&&false)){var t='(prefers-color-scheme: dark)',m=window.matchMedia(t);if(m.media!==t||m.matches){d.style.colorScheme = 'dark';c.add('dark')}else{d.style.colorScheme = 'light';c.add('light')}}else if(e){c.add(e|| '')}else{c.add('light')}if(e==='light'||e==='dark'||!e)d.style.colorScheme=e||'light'}catch(e){}}()</script><script src=\"/_next/static/chunks/webpack-e8afe3ae2f1a0a14.js\" async=\"\"></script><script>(self.__next_f=self.__next_f||[]).push([0]);self.__next_f.push([2,null])</script><script>self.__next_f.push([1,\"1:HL[\\\"/_next/static/media/a34f9d1faa5f3315-s.p.woff2\\\",\\\"font\\\",{\\\"crossOrigin\\\":\\\"\\\",\\\"type\\\":\\\"font/woff2\\\"}]\\n2:HL[\\\"/_next/static/media/bb3ef058b751a6ad-s.p.woff2\\\",\\\"font\\\",{\\\"crossOrigin\\\":\\\"\\\",\\\"type\\\":\\\"font/woff2\\\"}]\\n3:HL[\\\"/_next/static/css/df842cdd5139c39e.css\\\",\\\"style\\\"]\\n0:\\\"$L4\\\"\\n\"])</script><script>self.__next_f.push([1,\"5:HL[\\\"/_next/static/css/42c27cb71e996d58.css\\\",\\\"style\\\"]\\n\"])</script><script>self.__next_f.push([1,\"6:I[1720,[],\\\"\\\"]\\n8:I[8142,[],\\\"\\\"]\\n9:I[32614,[\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"3185\\\",\\\"static/chunks/app/layout-b3c5f4a3dd59966c.js\\\"],\\\"Toaster\\\"]\\na:I[64954,[\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\"])</script><script>self.__next_f.push([1,\"\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"3185\\\",\\\"static/chunks/app/layout-b3c5f4a3dd59966c.js\\\"],\\\"Providers\\\"]\\nb:I[65205,[],\\\"\\\"]\\nc:I[99788,[],\\\"\\\"]\\n\"])</script><script>self.__next_f.push([1,\"4:[[[\\\"$\\\",\\\"link\\\",\\\"0\\\",{\\\"rel\\\":\\\"stylesheet\\\",\\\"href\\\":\\\"/_next/static/css/df842cdd5139c39e.css\\\",\\\"precedence\\\":\\\"next\\\",\\\"crossOrigin\\\":\\\"$undefined\\\"}]],[\\\"$\\\",\\\"$L6\\\",null,{\\\"buildId\\\":\\\"stVtqBRqHzipXezTdWhs9\\\",\\\"assetPrefix\\\":\\\"\\\",\\\"initialCanonicalUrl\\\":\\\"/\\\",\\\"initialTree\\\":[\\\"\\\",{\\\"children\\\":[\\\"(chat)\\\",{\\\"children\\\":[\\\"__PAGE__\\\",{}]}]},\\\"$undefined\\\",\\\"$undefined\\\",true],\\\"initialHead\\\":[false,\\\"$L7\\\"],\\\"globalErrorComponent\\\":\\\"$8\\\",\\\"children\\\":[null,[\\\"$\\\",\\\"html\\\",null,{\\\"lang\\\":\\\"en\\\",\\\"suppressHydrationWarning\\\":true,\\\"children\\\":[[\\\"$\\\",\\\"head\\\",null,{}],[\\\"$\\\",\\\"body\\\",null,{\\\"className\\\":\\\"font-sans antialiased custom-scrollbar __variable_d65c78 __variable_3c557b\\\",\\\"children\\\":[[\\\"$\\\",\\\"$L9\\\",null,{}],[\\\"$\\\",\\\"$La\\\",null,{\\\"attribute\\\":\\\"class\\\",\\\"defaultTheme\\\":\\\"light\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex flex-col min-h-screen\\\",\\\"children\\\":[\\\"$\\\",\\\"main\\\",null,{\\\"className\\\":\\\"flex flex-col flex-1 bg-muted/50 dark:bg-bgDarkMain\\\",\\\"children\\\":[\\\"$\\\",\\\"$Lb\\\",null,{\\\"parallelRouterKey\\\":\\\"children\\\",\\\"segmentPath\\\":[\\\"children\\\"],\\\"loading\\\":\\\"$undefined\\\",\\\"loadingStyles\\\":\\\"$undefined\\\",\\\"loadingScripts\\\":\\\"$undefined\\\",\\\"hasLoading\\\":false,\\\"error\\\":\\\"$undefined\\\",\\\"errorStyles\\\":\\\"$undefined\\\",\\\"errorScripts\\\":\\\"$undefined\\\",\\\"template\\\":[\\\"$\\\",\\\"$Lc\\\",null,{}],\\\"templateStyles\\\":\\\"$undefined\\\",\\\"templateScripts\\\":\\\"$undefined\\\",\\\"notFound\\\":[[\\\"$\\\",\\\"title\\\",null,{\\\"children\\\":\\\"404: This page could not be found.\\\"}],[\\\"$\\\",\\\"div\\\",null,{\\\"style\\\":{\\\"fontFamily\\\":\\\"system-ui,\\\\\\\"Segoe UI\\\\\\\",Roboto,Helvetica,Arial,sans-serif,\\\\\\\"Apple Color Emoji\\\\\\\",\\\\\\\"Segoe UI Emoji\\\\\\\"\\\",\\\"height\\\":\\\"100vh\\\",\\\"textAlign\\\":\\\"center\\\",\\\"display\\\":\\\"flex\\\",\\\"flexDirection\\\":\\\"column\\\",\\\"alignItems\\\":\\\"center\\\",\\\"justifyContent\\\":\\\"center\\\"},\\\"children\\\":[\\\"$\\\",\\\"div\\\",null,{\\\"children\\\":[[\\\"$\\\",\\\"style\\\",null,{\\\"dangerouslySetInnerHTML\\\":{\\\"__html\\\":\\\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\\\"}}],[\\\"$\\\",\\\"h1\\\",null,{\\\"className\\\":\\\"next-error-h1\\\",\\\"style\\\":{\\\"display\\\":\\\"inline-block\\\",\\\"margin\\\":\\\"0 20px 0 0\\\",\\\"padding\\\":\\\"0 23px 0 0\\\",\\\"fontSize\\\":24,\\\"fontWeight\\\":500,\\\"verticalAlign\\\":\\\"top\\\",\\\"lineHeight\\\":\\\"49px\\\"},\\\"children\\\":\\\"404\\\"}],[\\\"$\\\",\\\"div\\\",null,{\\\"style\\\":{\\\"display\\\":\\\"inline-block\\\"},\\\"children\\\":[\\\"$\\\",\\\"h2\\\",null,{\\\"style\\\":{\\\"fontSize\\\":14,\\\"fontWeight\\\":400,\\\"lineHeight\\\":\\\"49px\\\",\\\"margin\\\":0},\\\"children\\\":\\\"This page could not be found.\\\"}]}]]}]}]],\\\"notFoundStyles\\\":[],\\\"childProp\\\":{\\\"current\\\":[null,\\\"$Ld\\\",null],\\\"segment\\\":\\\"(chat)\\\"},\\\"styles\\\":null}]}]}],null]}]]}]]}],null]}]]\\n\"])</script><script>self.__next_f.push([1,\"10:{\\\"fontFamily\\\":\\\"system-ui,\\\\\\\"Segoe UI\\\\\\\",Roboto,Helvetica,Arial,sans-serif,\\\\\\\"Apple Color Emoji\\\\\\\",\\\\\\\"Segoe UI Emoji\\\\\\\"\\\",\\\"height\\\":\\\"100vh\\\",\\\"textAlign\\\":\\\"center\\\",\\\"display\\\":\\\"flex\\\",\\\"flexDirection\\\":\\\"column\\\",\\\"alignItems\\\":\\\"center\\\",\\\"justifyContent\\\":\\\"center\\\"}\\n11:{\\\"display\\\":\\\"inline-block\\\",\\\"margin\\\":\\\"0 20px 0 0\\\",\\\"padding\\\":\\\"0 23px 0 0\\\",\\\"fontSize\\\":24,\\\"fontWeight\\\":500,\\\"verticalAlign\\\":\\\"top\\\",\\\"lineHeight\\\":\\\"49px\\\"}\\n12:{\\\"display\\\":\\\"inline-block\\\"}\\n13:{\\\"fontSize\\\":14,\\\"fontWeight\\\":400,\\\"lineHeight\\\":\\\"49px\\\",\\\"margin\\\":0}\\n\"])</script><script>self.__next_f.push([1,\"d:[\\\"$Le\\\",[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"relative flex h-[calc(100vh_-_theme(spacing.16)_-_2.5em_+_5px)] overflow-hidden\\\",\\\"children\\\":[\\\"$Lf\\\",[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"fixed group w-full overflow-auto pl-0 animate-in duration-300 ease-in-out\\\",\\\"style\\\":{\\\"height\\\":\\\"-webkit-fill-available\\\"},\\\"children\\\":[\\\"$\\\",\\\"$Lb\\\",null,{\\\"parallelRouterKey\\\":\\\"children\\\",\\\"segmentPath\\\":[\\\"children\\\",\\\"(chat)\\\",\\\"children\\\"],\\\"loading\\\":\\\"$undefined\\\",\\\"loadingStyles\\\":\\\"$undefined\\\",\\\"loadingScripts\\\":\\\"$undefined\\\",\\\"hasLoading\\\":false,\\\"error\\\":\\\"$undefined\\\",\\\"errorStyles\\\":\\\"$undefined\\\",\\\"errorScripts\\\":\\\"$undefined\\\",\\\"template\\\":[\\\"$\\\",\\\"$Lc\\\",null,{}],\\\"templateStyles\\\":\\\"$undefined\\\",\\\"templateScripts\\\":\\\"$undefined\\\",\\\"notFound\\\":[[\\\"$\\\",\\\"title\\\",null,{\\\"children\\\":\\\"404: This page could not be found.\\\"}],[\\\"$\\\",\\\"div\\\",null,{\\\"style\\\":\\\"$10\\\",\\\"children\\\":[\\\"$\\\",\\\"div\\\",null,{\\\"children\\\":[[\\\"$\\\",\\\"style\\\",null,{\\\"dangerouslySetInnerHTML\\\":{\\\"__html\\\":\\\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\\\"}}],[\\\"$\\\",\\\"h1\\\",null,{\\\"className\\\":\\\"next-error-h1\\\",\\\"style\\\":\\\"$11\\\",\\\"children\\\":\\\"404\\\"}],[\\\"$\\\",\\\"div\\\",null,{\\\"style\\\":\\\"$12\\\",\\\"children\\\":[\\\"$\\\",\\\"h2\\\",null,{\\\"style\\\":\\\"$13\\\",\\\"children\\\":\\\"This page could not be found.\\\"}]}]]}]}]],\\\"notFoundStyles\\\":[],\\\"childProp\\\":{\\\"current\\\":[\\\"$L14\\\",\\\"$L15\\\",null],\\\"segment\\\":\\\"__PAGE__\\\"},\\\"styles\\\":[[\\\"$\\\",\\\"link\\\",\\\"0\\\",{\\\"rel\\\":\\\"stylesheet\\\",\\\"href\\\":\\\"/_next/static/css/42c27cb71e996d58.css\\\",\\\"precedence\\\":\\\"next\\\",\\\"crossOrigin\\\":\\\"$undefined\\\"}]]}]}]]}]]\\n\"])</script><script>self.__next_f.push([1,\"7:[[\\\"$\\\",\\\"meta\\\",\\\"0\\\",{\\\"name\\\":\\\"viewport\\\",\\\"content\\\":\\\"width=device-width, initial-scale=1\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"1\\\",{\\\"charSet\\\":\\\"utf-8\\\"}],[\\\"$\\\",\\\"title\\\",\\\"2\\\",{\\\"children\\\":\\\"Chat Blackbox: AI Code Generation, Code Chat, Code Search\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"3\\\",{\\\"name\\\":\\\"description\\\",\\\"content\\\":\\\"BLACKBOX AI is the Best AI Model for Code. Millions of developers use Blackbox Code Chat to answer coding questions and assist them while writing code faster. Whether you are fixing a bug, building a new feature or refactoring your code, ask BLACKBOX to help.\\\\n\\\\nBLACKBOX has real-time knowledge of the world, making it able to answer questions about recent events, technological breakthroughs, product releases, API documentations \\u0026 more\\\\n\\\\nBLACKBOX integrates directly with VSCode to automatically suggests the next lines of code based on your repo context.\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"4\\\",{\\\"name\\\":\\\"keywords\\\",\\\"content\\\":\\\"blackbox, blackboxai,ai,chat,autocomplete,bash,c,c#,c++,code-recommendation,cpp,csharp,css,domination,go,golang,haskell,html,intellicode,intellisense,java,javascript,julia,jupyter,keybindings,kite,kotlin,lua,method\\u0026#32;completion,node,node.js,nodejs,objectivec,objective-c,ocaml,perl,php,python,react,ruby,rust,snippets,swift,typescript\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"5\\\",{\\\"property\\\":\\\"og:image:type\\\",\\\"content\\\":\\\"image/png\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"6\\\",{\\\"property\\\":\\\"og:image:width\\\",\\\"content\\\":\\\"1686\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"7\\\",{\\\"property\\\":\\\"og:image:height\\\",\\\"content\\\":\\\"882\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"8\\\",{\\\"property\\\":\\\"og:image\\\",\\\"content\\\":\\\"https://https/www.blackbox.ai/opengraph-image.png?49c2c3ea917a06c7\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"9\\\",{\\\"name\\\":\\\"twitter:card\\\",\\\"content\\\":\\\"summary_large_image\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"10\\\",{\\\"name\\\":\\\"twitter:image:type\\\",\\\"content\\\":\\\"image/png\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"11\\\",{\\\"name\\\":\\\"twitter:image:width\\\",\\\"content\\\":\\\"1686\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"12\\\",{\\\"name\\\":\\\"twitter:image:height\\\",\\\"content\\\":\\\"882\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"13\\\",{\\\"name\\\":\\\"twitter:image\\\",\\\"content\\\":\\\"https://https/www.blackbox.ai/twitter-image.png?49c2c3ea917a06c7\\\"}],[\\\"$\\\",\\\"link\\\",\\\"14\\\",{\\\"rel\\\":\\\"shortcut icon\\\",\\\"href\\\":\\\"/favicon-16x16.png\\\"}],[\\\"$\\\",\\\"link\\\",\\\"15\\\",{\\\"rel\\\":\\\"icon\\\",\\\"href\\\":\\\"/favicon.ico\\\"}],[\\\"$\\\",\\\"link\\\",\\\"16\\\",{\\\"rel\\\":\\\"apple-touch-icon\\\",\\\"href\\\":\\\"/apple-touch-icon.png\\\"}],[\\\"$\\\",\\\"meta\\\",\\\"17\\\",{\\\"name\\\":\\\"next-size-adjust\\\"}]]\\n\"])</script><script>self.__next_f.push([1,\"16:I[94620,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"Sidebar\\\"]\\n\"])</script><script>self.__next_f.push([1,\"18:I[1744,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"742\\\",\\\"static/chunks/a00912cf-8590a8015a579639.js\\\",\\\"748\\\",\\\"static/chunks/b27dc69b-f6827517fb76ef75.js\\\",\\\"5793\\\",\\\"static/chunks/37f960d4-e3e90f71c5f3e0a5.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"5548\\\",\\\"static/chunks/5548-45a2e54c772da090.js\\\",\\\"1973\\\",\\\"static/chunks/1973-75dc77d25403234c.js\\\",\\\"8155\\\",\\\"static/chunks/8155-b453e29f2c977bb8.js\\\",\\\"5219\\\",\\\"static/chunks/5219-90aac1761166910c.js\\\",\\\"8473\\\",\\\"static/chunks/8473-88d40eadac9d9130.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"3229\\\",\\\"static/chunks/3229-24779011567e041f.js\\\",\\\"3559\\\",\\\"static/chunks/3559-b6cb22e9bbafc9cc.js\\\",\\\"5338\\\",\\\"static/chunks/app/(chat)/page-d137c9273487f249.js\\\"],\\\"ChatMainPage\\\"]\\n\"])</script><script>self.__next_f.push([1,\"19:I[18867,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"742\\\",\\\"static/chunks/a00912cf-8590a8015a579639.js\\\",\\\"748\\\",\\\"static/chunks/b27dc69b-f6827517fb76ef75.js\\\",\\\"5793\\\",\\\"static/chunks/37f960d4-e3e90f71c5f3e0a5.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"5548\\\",\\\"static/chunks/5548-45a2e54c772da090.js\\\",\\\"1973\\\",\\\"static/chunks/1973-75dc77d25403234c.js\\\",\\\"8155\\\",\\\"static/chunks/8155-b453e29f2c977bb8.js\\\",\\\"5219\\\",\\\"static/chunks/5219-90aac1761166910c.js\\\",\\\"8473\\\",\\\"static/chunks/8473-88d40eadac9d9130.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"3229\\\",\\\"static/chunks/3229-24779011567e041f.js\\\",\\\"3559\\\",\\\"static/chunks/3559-b6cb22e9bbafc9cc.js\\\",\\\"5338\\\",\\\"static/chunks/app/(chat)/page-d137c9273487f249.js\\\"],\\\"GoogleOneTapController\\\"]\\n\"])</script><script>self.__next_f.push([1,\"1a:I[45462,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"SidebarMobile\\\"]\\n\"])</script><script>self.__next_f.push([1,\"1c:I[93390,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"SidebarToggle\\\"]\\n\"])</script><script>self.__next_f.push([1,\"1d:I[38261,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"HeaderModelSelection\\\"]\\n\"])</script><script>self.__next_f.push([1,\"1e:I[57879,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"Tracker\\\"]\\n\"])</script><script>self.__next_f.push([1,\"1f:I[17730,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"HeaderThemeButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"20:I[86108,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"InviteButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"21:I[84667,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"NewChatMobileButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"22:I[69576,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"\\\"]\\n\"])</script><script>self.__next_f.push([1,\"23:I[56502,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"ImageGenerationButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"24:I[48892,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"\\\"]\\n\"])</script><script>self.__next_f.push([1,\"25:I[74483,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"ImageToCodeButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"26:I[36176,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"CreateOrEditAgentButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"27:I[98808,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"WelcomeButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"28:I[54207,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"JetBrainsButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"29:I[72541,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"VscodeButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"2a:I[83292,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"LoginButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"f:[\\\"$\\\",\\\"$L16\\\",null,{\\\"className\\\":\\\"peer absolute inset-y-0 z-30 hidden -translate-x-full border-r duration-300 ease-in-out data-[state=open]:translate-x-0 mob-flex lg:w-[250px] xl:w-[240px]\\\",\\\"children\\\":\\\"$L17\\\"}]\\n15:[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"relative flex h-[calc(100vh_-_theme(spacing.16)_-_2.5em_+_5px)] overflow-hidden\\\",\\\"children\\\":[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"fixed group w-full overflow-auto custom-scrollbar pl-0 animate-in duration-300 ease-in-out\\\",\\\"style\\\":{\\\"height\\\":\\\"-webkit-fill-available\\\"},\\\"children\\\":[\"])</script><script>self.__next_f.push([1,\"[\\\"$\\\",\\\"$L18\\\",null,{\\\"initialFiles\\\":\\\"$undefined\\\"}],[\\\"$\\\",\\\"$L19\\\",null,{}]]}]}]\\n14:null\\n\"])</script><script>self.__next_f.push([1,\"e:[\\\"$\\\",\\\"header\\\",null,{\\\"className\\\":\\\"sticky top-0 z-50 flex items-center justify-between w-full h-16 px-4 shrink-0 from-background/10 via-background/50\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex items-center\\\",\\\"children\\\":[[\\\"$\\\",\\\"$L1a\\\",null,{\\\"children\\\":\\\"$L1b\\\"}],[\\\"$\\\",\\\"$L1c\\\",null,{}],[\\\"$\\\",\\\"$L1d\\\",null,{\\\"session\\\":null}]]}],[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex items-center justify-end space-x-2\\\",\\\"children\\\":[[\\\"$\\\",\\\"$L1e\\\",null,{}],[\\\"$\\\",\\\"$L1f\\\",null,{}],[\\\"$\\\",\\\"$L20\\\",null,{\\\"position\\\":\\\"header\\\"}],[\\\"$\\\",\\\"$L21\\\",null,{}],[\\\"$\\\",\\\"$L22\\\",null,{}],[\\\"$\\\",\\\"$L23\\\",null,{\\\"session\\\":null}],[\\\"$\\\",\\\"$L24\\\",null,{}],[\\\"$\\\",\\\"$L25\\\",null,{\\\"session\\\":null}],[\\\"$\\\",\\\"$L26\\\",null,{\\\"position\\\":\\\"header\\\"}],[\\\"$\\\",\\\"$L27\\\",null,{}],[\\\"$\\\",\\\"$L28\\\",null,{}],[\\\"$\\\",\\\"$L29\\\",null,{}],[\\\"$\\\",\\\"$L2a\\\",null,{}],\\\"$undefined\\\"]}]]}]\\n\"])</script><script>self.__next_f.push([1,\"2b:I[81622,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"NewChatButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"2c:I[88980,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"RoboCoder\\\"]\\n\"])</script><script>self.__next_f.push([1,\"2d:I[85247,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"ImageGenSidenavButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"2e:I[86064,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"ImageToAppSidenavButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"2f:I[92291,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"SidebarWorkspaceButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"30:I[55875,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"DesktopDownload\\\"]\\n\"])</script><script>self.__next_f.push([1,\"31:I[24433,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"BlogsButton\\\"]\\n\"])</script><script>self.__next_f.push([1,\"32:\\\"$Sreact.suspense\\\"\\n\"])</script><script>self.__next_f.push([1,\"33:I[24060,[\\\"8791\\\",\\\"static/chunks/08ffd5a1-1efe9e750f7699f3.js\\\",\\\"1413\\\",\\\"static/chunks/3f9dfec0-695648b36cb4c167.js\\\",\\\"5153\\\",\\\"static/chunks/5153-58ea3da6f0a31254.js\\\",\\\"3447\\\",\\\"static/chunks/3447-bd02a654a85949f7.js\\\",\\\"5864\\\",\\\"static/chunks/5864-cc364f2dfdce9d21.js\\\",\\\"9616\\\",\\\"static/chunks/9616-28ba65db0942affe.js\\\",\\\"3329\\\",\\\"static/chunks/3329-78ba1eeca6971ead.js\\\",\\\"6272\\\",\\\"static/chunks/6272-e3b5ade80a66c056.js\\\",\\\"4836\\\",\\\"static/chunks/4836-953da52b268fd9a5.js\\\",\\\"6973\\\",\\\"static/chunks/6973-8fc05488bb278fd2.js\\\",\\\"4427\\\",\\\"static/chunks/4427-feb350a99b7ab226.js\\\",\\\"7968\\\",\\\"static/chunks/7968-4c3079258bc08265.js\\\",\\\"9457\\\",\\\"static/chunks/9457-a66dee0b2ff78680.js\\\",\\\"4178\\\",\\\"static/chunks/4178-345df8144d676d40.js\\\",\\\"2052\\\",\\\"static/chunks/2052-085024e2d1c11778.js\\\",\\\"7376\\\",\\\"static/chunks/7376-b4519753e117adf8.js\\\",\\\"5170\\\",\\\"static/chunks/5170-334da3aeeaf6b4e7.js\\\",\\\"283\\\",\\\"static/chunks/app/(chat)/layout-65323d58093f337a.js\\\"],\\\"SidebarList\\\"]\\n\"])</script><script>self.__next_f.push([1,\"17:[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex flex-col h-full mb-10 bg-zinc-50 dark:bg-bgDarkMain\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"p-2 space-y-2 overflow-y-auto\\\",\\\"children\\\":[[\\\"$\\\",\\\"$L2b\\\",null,{}],[\\\"$\\\",\\\"$L26\\\",null,{\\\"position\\\":\\\"sidebar\\\"}],[\\\"$\\\",\\\"$L2c\\\",null,{\\\"session\\\":null,\\\"from\\\":\\\"sidenav\\\"}],[\\\"$\\\",\\\"$L2d\\\",null,{}],[\\\"$\\\",\\\"$L2e\\\",null,{}],[\\\"$\\\",\\\"$L2f\\\",null,{}],[\\\"$\\\",\\\"$L30\\\",null,{}],[\\\"$\\\",\\\"$L31\\\",null,{}]]}],[\\\"$\\\",\\\"$32\\\",null,{\\\"fallback\\\":[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex flex-col flex-1 px-4 space-y-4 overflow-auto\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",\\\"0\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"1\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"2\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"3\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"4\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"5\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"6\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"7\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"8\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"9\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}]]}],\\\"children\\\":[\\\"$\\\",\\\"$L33\\\",null,{\\\"userId\\\":\\\"f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf\\\"}]}]]}]\\n\"])</script><script>self.__next_f.push([1,\"1b:[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex flex-col h-full mb-10 bg-zinc-50 dark:bg-bgDarkMain\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"p-2 space-y-2 overflow-y-auto\\\",\\\"children\\\":[[\\\"$\\\",\\\"$L2b\\\",null,{}],[\\\"$\\\",\\\"$L26\\\",null,{\\\"position\\\":\\\"sidebar\\\"}],[\\\"$\\\",\\\"$L2c\\\",null,{\\\"session\\\":null,\\\"from\\\":\\\"sidenav\\\"}],[\\\"$\\\",\\\"$L2d\\\",null,{}],[\\\"$\\\",\\\"$L2e\\\",null,{}],[\\\"$\\\",\\\"$L2f\\\",null,{}],[\\\"$\\\",\\\"$L30\\\",null,{}],[\\\"$\\\",\\\"$L31\\\",null,{}]]}],[\\\"$\\\",\\\"$32\\\",null,{\\\"fallback\\\":[\\\"$\\\",\\\"div\\\",null,{\\\"className\\\":\\\"flex flex-col flex-1 px-4 space-y-4 overflow-auto\\\",\\\"children\\\":[[\\\"$\\\",\\\"div\\\",\\\"0\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"1\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"2\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"3\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"4\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"5\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"6\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"7\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"8\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}],[\\\"$\\\",\\\"div\\\",\\\"9\\\",{\\\"className\\\":\\\"w-full h-6 rounded-md shrink-0 animate-pulse bg-zinc-200 dark:bg-zinc-800\\\"}]]}],\\\"children\\\":[\\\"$\\\",\\\"$L33\\\",null,{\\\"userId\\\":\\\"f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf\\\"}]}]]}]\\n\"])</script><script>self.__next_f.push([1,\"\"])</script></body></html>",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 4. Carbon

**Args:**
  - **query (str)**: Potongan kode yang akan dirender sebagai gambar.

**Description**:
Return: FilePath: Jalur file dari gambar yang disimpan.

```python
from ApiNyaEr import apinya

result = await apinya.carbon(query='Tidur')
print(result)
```

#### Expected Output

```text
/home/runner/work/ApiNyaEr/ApiNyaEr/downloads/carbon_lXXP9x71.png
```

### 5. Cat

**Description**:
Generate random gambar kucing.

**Returns:**
  - **str or None**: Url random kucing ataupun None; None jika response
    tidak di terima.

```python
from ApiNyaEr import apinya

result = await apinya.cat()
print(result)
```

#### Expected Output

```text
https://cdn2.thecatapi.com/images/7kl.jpg
```

### 6. Dare

**Description**:
Dapatkan Kata kata dare

**Returns:**
  - **str**: Random kata dare

```python
from ApiNyaEr import apinya

result = await apinya.dare()
print(result)
```

#### Expected Output

```text
Minum tiga teguk teh atau coke (coca-cola atau sprite) yang dicampur sambal.
```

### 7. Doa

**Description**:
Mengambil data doa dari API ItzPire berdasarkan nama doa.

**Args:**
  - **nama_doa (str)**: Nama doa yang ingin diambil.

**Returns:**
  - **str**: Teks doa yang diformat dengan rapi termasuk doa, ayat, latin, dan artinya.

```python
from ApiNyaEr import apinya

result = await apinya.doa(nama_doa='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 504, message='Gateway Time-out', url='https://itzpire.com/religion/islamic/doa?doaName=Tidur'
```

### 8. Dog

**Description**:
Dapatkan random foto anjing.

**Returns:**
  - **str or None**: Url Random anjing jika tersedia; None jika tidak ada
    response yang di terima.

```python
from ApiNyaEr import apinya

result = await apinya.dog()
print(result)
```

#### Expected Output

```text
https://random.dog/63bb7640-708d-4bba-a6d5-af527b94254b.jpg
```

### 9. Fakta Unik

**Description**:
Dapatkan random Seputar Fakta Unik

**Returns:**
  - **str**: Random Fakta

```python
from ApiNyaEr import apinya

result = await apinya.fakta_unik()
print(result)
```

#### Expected Output

```text
🌾 **Tidak ada bukti yang pasti siapa yang membangun Taj Mahal.**
```

### 10. Gemini

**Description**:
Berinteraksi dengan Gemini AI. ✨

**Args:**
  - **tanya (str)**: Teks yang di berikan.

**Returns:**
  - **dict**: dictionaries yang berisi konten ai nya.

```python
from ApiNyaEr import apinya

result = await apinya.gemini(tanya='Tidur')
print(result)
```

#### Expected Output

```text
None
```

### 11. Get Pinter Url

**Description**:
Mengembalikan hasil request Pinterest berdasarkan query yang diberikan.

**Args:**
  - **query (str)**: Kata kunci pencarian untuk Pinterest.

**Returns:**
  - **dict**: Respons JSON dari API Pinterest.

```python
from ApiNyaEr import apinya

result = await apinya.get_pinter_url(query='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 403, message='Forbidden', url='https://api.ryzendesu.vip/api/search/pinterest?query=Tidur'
```

### 12. Github Search

**Description**:
Pencarian GitHub untuk beberapa tipe konten.

**Args:**
  - **cari (str)**: untuk Pencarian.
  - **tipe (str, optional)**: Type pencarian, terdiri dari:
    - "repositories"
    - "users"
    - "organizations"
    - "issues"
    - "pull_requests"
    - "commits"
    - "topics"

**Description**:
Defaults ke "repositories". max_results (int, optional): Maximum nomor dari results untuk return. Defaultnya 3.

**Returns:**
  - **list**: List dari pencarian results atau pesan error.

```python
from ApiNyaEr import apinya

result = await apinya.github_search(cari='Tidur', tipe='repositories', max_results=3)
print(result)
```

#### Expected Output

```json
[
    {
        "name": "rs-bed-covid-indo-api",
        "full_name": "satyawikananda/rs-bed-covid-indo-api",
        "description": "API ketersediaan rumah sakit dan tempat tidur rumah sakit untuk pasien covid-19 ataupun non-covid yang berada di Indonesia",
        "url": "https://github.com/satyawikananda/rs-bed-covid-indo-api",
        "language": "TypeScript",
        "stargazers_count": 113,
        "forks_count": 25
    },
    {
        "name": "bed-covid-rs-indo",
        "full_name": "hendraaagil/bed-covid-rs-indo",
        "description": "Website yang memberikan informasi terkait ketersediaan rumah sakit dan tempat tidur rumah sakit untuk pasien covid-19 ataupun non-covid di Indonesia.",
        "url": "https://github.com/hendraaagil/bed-covid-rs-indo",
        "language": "JavaScript",
        "stargazers_count": 23,
        "forks_count": 3
    },
    {
        "name": "hobikoding.github.io",
        "full_name": "hobikoding/hobikoding.github.io",
        "description": ":rose: Hobikoding - Mari ngoding sambil tidur",
        "url": "https://github.com/hobikoding/hobikoding.github.io",
        "language": "Makefile",
        "stargazers_count": 3,
        "forks_count": 0
    }
]
```

### 13. Hug

**Description**:
Dapatkan gif Random pelukan dari Nekos.Best API.

**Args:**
  - **amount (int)**: amount gambar nya, Defaultnya 1.

**Returns:**
  - **list**: List dari dictionaries tentang informasi neko image atau GIF.
    Type dictionaries:
    - anime_name (str): Nama anime.
    - url (str): Url gif nya.

```python
from ApiNyaEr import apinya

result = await apinya.hug(amount=1)
print(result)
```

#### Expected Output

```json
[
    {
        "anime_name": "Engage Kiss",
        "url": "https://nekos.best/api/v2/hug/c968b89d-494e-453d-95b7-bd5f3d238e4e.gif"
    }
]
```

### 14. Kapan Libur

**Description**:
Dapatkan informasi Hari libur kedepan.

**Returns:**
  - **str**: Hari Libur Berikutnya.

```python
from ApiNyaEr import apinya

result = await apinya.kapan_libur()
print(result)
```

#### Expected Output

```text
Expecting value: line 1 column 1 (char 0)
```

### 15. Luminai

**Args:**
  - **tanya (str)**: Teks query

**Returns:**
    resultnya

```python
from ApiNyaEr import apinya

result = await apinya.luminai(tanya='Tidur')
print(result)
```

#### Expected Output

```json
{
    "resultnya": "Tidur itu penting banget, bro! \ud83d\ude34 Biar badan dan otak kita bisa recharge. Kapan terakhir kali kamu tidur nyenyak? \ud83d\udca4\u2728",
    "join": "@Er_Support_Group",
    "success": true
}
```

### 16. Nama Epep

**Description**:
Dapatkan random nama ep ep

**Returns:**
  - **str**: Random nama ep epnya

```python
from ApiNyaEr import apinya

result = await apinya.nama_epep()
print(result)
```

#### Expected Output

```text
꧁✮ꌗꍏꌩꍏꈤꀘ✮꧂
```

### 17. Password

**Description**:
Fungsi ini menghasilkan kata sandi acak dengan menggabungkan huruf besar, huruf kecil, tanda baca, dan digit.

**Description**:
Parameters: - num (int): Panjang kata sandi yang dihasilkan. Default adalah 12 jika tidak ditentukan.

**Returns:**
**Description**:
- str: Kata sandi yang dihasilkan secara acak yang terdiri dari karakter dari string.ascii_letters, string.punctuation, dan string.digits.

```python
from ApiNyaEr import apinya

result = await apinya.password(num=12)
print(result)
```

#### Expected Output

```text
h<B>Ddi96ePl
```

### 18. Pypi

**Description**:
Mengambil informasi metadata tentang paket Python tertentu dari API PyPI.

**Args:**
  - **namanya (str)**: Nama paket yang dicari di PyPI.

**Returns:**
  - **dict atau None**: Sebuah kamus dengan informasi relevan tentang paket jika ditemukan, yang berisi:
    - name (str): Nama paket.
    - version (str): Versi terbaru paket.
    - summary (str): Deskripsi singkat tentang paket.
    - author (str): Penulis paket.
    - author_email (str): Email penulis paket.
    - license (str): Jenis lisensi.
    - home_page (str): URL halaman utama paket.
    - package_url (str): URL paket di PyPI.
    - requires_python (str): Versi Python minimum yang dibutuhkan.
    - keywords (str): Kata kunci yang terkait dengan paket.
    - classifiers (list): Daftar pengklasifikasi PyPI.
    - project_urls (dict): URL proyek tambahan (misalnya, kode sumber, dokumentasi).
**Description**:
Returns None jika paket tidak ditemukan atau terjadi kesalahan.

```python
from ApiNyaEr import apinya

result = await apinya.pypi(namanya='Tidur')
print(result)
```

#### Expected Output

```text
Request failed: 404, message='Not Found', url='https://pypi.org/pypi/Tidur/json'
```

### 19. Qanime

**Description**:
Dapatkan Kata kata anime

**Returns:**
  - **str**: Random kata anime

```python
from ApiNyaEr import apinya

result = await apinya.qanime()
print(result)
```

#### Expected Output

```json
{
    "\ud83c\udf81 **Quotes": "Kadang-kadang pria harus melindungi sesuatu, walaupun dia harus membuang kehormatannya sendiri.**",
    "\ud83c\udf39 **Character": "Kanichi Konishi**",
    "\ud83c\udf41 **Anime": "Shokugeki no Souma**",
    "\ud83c\udf41 **Episode": "Episode 6**"
}
```

### 20. Qhacker

**Description**:
Dapatkan random Quotes Hacker

**Returns:**
  - **str**: Random Quotes Hacker

```python
from ApiNyaEr import apinya

result = await apinya.qhacker()
print(result)
```

#### Expected Output

```text
🃏 **Anda tidak dapat meretas takdir, kekuatan kasar... Anda perlu pintu belakang, saluran samping ke dalam hidup.**
```

### 21. Qislam

**Description**:
Dapatkan random Quotes Islamic

**Returns:**
  - **str**: Random Quotes Islam

```python
from ApiNyaEr import apinya

result = await apinya.qislam()
print(result)
```

#### Expected Output

```text
📖 **Musibah yang membuatmu kembali kepada Allah lebih baik dari nikmat yang membuatmu lupa kepada Allah**
```

### 22. Qpubg

**Description**:
Dapatkan random Quotes pubg

**Returns:**
  - **str**: Random Quotes Pubg

```python
from ApiNyaEr import apinya

result = await apinya.qpubg()
print(result)
```

#### Expected Output

```text
🏆 **Aku tidak pernah menyukai chicken, tapi tidak dengan chicken di PUBG**
```

### 23. Truth

**Description**:
Dapatkan Kata kata truth

**Returns:**
  - **str**: Random kata truth

```python
from ApiNyaEr import apinya

result = await apinya.truth()
print(result)
```

#### Expected Output

```text
Hal paling romantis apa yang seseorang (beda gender) pernah lakuin atau kasih ke kamu?
```

### 24. Wibu

**Description**:
Fetch spesifik Gambar/Gif Anime.

**Args:**
  - **endpoint (str)**: Kategori endpoin gambar/Gif animenya. Defaultnya
    "kiss".
    Valid Format endpoints:
    - "husbando", "kitsune", "neko", "waifu"
    Valid GIF endpoints:
    - "baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm",
    "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick",
    "kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke",
    "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug",
    "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"
    amount (int): jumlah item gambarnya. Default 1.

**Returns:**
  - **dict**: Dictionary konten yang di request. Dictionarynya memiliki kata
    kunci`"results"`,
    yang menampung limit.

**Raises:**
  - **ValueError**: Jika endpoint tidak valid.

```python
from ApiNyaEr import apinya

result = await apinya.wibu(endpoint='kiss', amount=1)
print(result)
```

#### Expected Output

```json
{
    "results": [
        {
            "anime_name": "Death Note",
            "url": "https://nekos.best/api/v2/kiss/de8b5bde-dba5-437e-98a4-a48123f9809c.gif"
        }
    ]
}
```


This Project is Licensed under [GNU General Public License](https://github.com/ErRickow/ApiNyaEr/blob/Er/LICENSE)