# Markdown.
Markdown is a text-to-HTML conversion tool for web writers. Markdown allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML).

## Online tools:
- [stackedit](https://stackedit.io/) Testing Markdown online.

## Index
- [Headers 1 to 6 examples.](#headers)
- [Text formats: Italic, Strong, Strikethrought.](#text-format)
- [Horizontal Rules.](#horizontal-rule)
- [Scape special character.](#scape-special-character)
- [Blockquote.](#blockquote)
- [Inline Code Block.](#inline-code-block)
- [Lists.](#lists)
- [Task List.](#task-list)
- [Tables.](#tables)
- [Links.](#links)
- [Images.](#images)
- [Code Markdowns.](#github-markdown)
- [Go to the end.](#endfile)

--- 

<!-- HEADERS. -->
## Headers

```
# Heading 1
##  Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```
---
# Heading 1
##  Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

[Back to Index.](#index)
---

<!-- Text formats. -->
## Text format
- Italics: *This text* is italic. _This text_ is italic.
- Strong: **This text** is strong. __This text__ is strong.
- Italics and strong: ***This text*** is italic and strong. ___This text___ is italic and strong.
- Strikethrough (tachado):  ~~This text~~ is strikethrough
[Back to Index.](#index)
---

<!-- # HORIZONTAL -->
## Horizontal Rule
    Need to write 
        - - - 
        or 
        ___
        in order to get a horizontal rule.
- - -
___
[Back to Index.](#index)

## Scape special character
    \\	    backslash
    \`  	    backtick (see also escaping backticks in code)
    \*	    asterisk
    \_	    underscore
    \{ \}	    curly braces
    \[ \]	    brackets
    \< \>	    angle brackets
    \( \)	    parentheses
    \#	    pound sign
    \+	    plus sign
    \-	    minus sign (hyphen)
    \.	    dot
    \!	    exclamation mark
    \|	    pipe (see also escaping pipe in tables)
[Back to Index.](#index)

## Blockquote
> This is a quote. "In at justo et quam pulvinar accumsan. Morbi non arcu accumsan, efficitur mauris et, blandit lectus. Nam arcu felis, tempor in nisl quis, tincidunt placerat arcu. Sed accumsan, orci sit amet lacinia gravida, tellus est dignissim diam, eget sollicitudin elit felis vitae tellus. Etiam lacinia urna ac bibendum lacinia. Phasellus iaculis quam et nulla volutpat scelerisque. Duis ac sem vestibulum, dapibus ligula vel, feugiat urna."

[Back to Index.](#index)

## Inline code Block
Normally 4 spaces or ona tab
    
    In at justo et quam pulvinar accumsan. Morbi non arcu accumsan, efficitur mauris et, blandit lectus. Nam arcu felis, tempor in nisl quis, tincidunt placerat arcu. Sed accumsan, orci sit amet lacinia gravida, . 
This is a Note [^note]

[Back to Index.](#index)

## Lists
* Item 1
* Item 2
* Item 3
   * Nested Item 1
   * Nested Item 2
        * Nested Item 1

1. Item 1
1. Item 2
1. Item 3
   1. nested Item 1
   1. nested Item 2
        1. Nested Item 1

[Back to Index.](#index)

## Task List
* [x] Task 1
* [x] Task 2
* [ ] Task 3
   * [x] Test 1

[Back to Index.](#index)

## Tables
    | Name          | Email             | ID            |
    | ---           | :---:             | ---:          |
    | John Doe      | john@gmail.com    | 123           |
    | Jane Doe      | jane@gmail.com    | 456           |
    | Aligned Left | Aligned Center     | Aligned Right |

| Name      | Email                         | ID |
| --- | :---:| ---: |
| John Doe | john@gmail.com | 123 |
| Jane Doe | jane@gmail.com | 456 |
| Aligned Left | Aligned Center | Aligned Right |

[Back to Index.](#index)

## Links 
    - [Google](http://www.google.com "This is text over this url.")
Result: [Google](http://www.google.com "This is text over this url.")

    - Save a url in a key, then use it again:

[key]:https//www.google.com
Result: [Google url again!][key]

[Back to Index.](#index)


## Images
`![Markdown Logo](https://markdown-here.com/img/icon256.png "tal vez hay texto")`
![Markdown Logo](https://markdown-here.com/img/icon256.png "tal vez hay texto")

[Back to Index.](#index)


# Github Markdown
## Code Blocks
         Esto es un codigo.

Tambien puedes usar `codigo` asi.
```bash
npm install 
npm start
```
```javascript
 funtion add (num1, num2) {
   return num1 + num2;
}
```

```python 
  def add (num1, num2):
   return num1 + num2
```
</body>

<!-- ADITIONAL CONTENT $-->
<style>
   p {
      color: green
   }
</style>

--- 
# Testing comments
1. one two <!-- three -->
2. one two <# three -->
[](one two three)
.comment { display :none;}
// one two three
{>> one two three<<}
---
<!-- you can jump to this id: "endfile" -->
##### end of this file.<a id="endfile"></a>

[^note]: This is a note
