# For part_contents.txt
#
# make hyperlinks

# For part_content.txt
#
# idea: check code point of first character,
# if it's in the range of greek, apply a CSS class

# if first word is number and first char of second word
# is A-Z, then make it a header

# For part_appendix.txt
#
# create headers only

if __name__ == "__main__":
    print("Converting part_* files")

    with open('index.html', 'w', encoding="utf-8") as html:
        print("""
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Guia de Conversação de Grego</title>
        <style>

        @font-face {
        font-family: 'GFSNeoH';
        src: url('gfsneoh.ttf') format('truetype');
        font-style: normal;
        }

        @font-face {
        font-family: 'NotoSans';
        src: url('notosans.ttf') format('truetype');
        font-style: normal;
        }

        body {
        margin: 1.2em;
        }
        
        .sp {
        font-size: 0.3em;
        margin: 0.2em;
        }
        
        .gr {
        font-family: 'GFSNeoH';
        font-size: 125%;
        background-color: #DEF;
        padding: 0.3em;
        }

        pre {
        font-family: 'GFSNeoH';
        font-size: 125%;
        background-color: #DEF;
        padding: 0.3em;
        }

        .pt {
        padding: 0.3em;
        font-family: 'NotoSans';
        }
        
        a {
        display: block;
        text-decoration: none;
        font-family: 'NotoSans';
        margin: 0.3em;
        }

        .sect {
        font-size: 2em;
        margin: 0.8em 0 0.4em 0;
        }

        .back {
        position: fixed;
        bottom: 1.5em;
        right: 1em;
        background-color: #FFF;
        border: 2px solid #CCC;
        border-radius: 5px;
        box-shadow: 5px 5px 2px #CCC;

        }
        
        </style>
        
    </head>
    <body>
        <div class="back"><a href="#top">Voltar ao topo</a></div>
        <div id="top" class="sect">GUIA DE CONVERSAÇÃO DE GREGO</div>
        
""", file=html)

        for line in open("part_contents.txt", encoding="utf-8"):
            line = line.strip()
            if len(line) > 1:
                parts = line.split()
                
                id, name = parts[0], parts[1:]
                
                print('<a id="a{}" href="#p{}">{}</a>'.format(id, id, " ".join(name)), file=html)
                

        for line in open("part_content.txt", encoding="utf-8"):
            line = line.strip()

            if len(line) > 1:
                firstchar = line[0]
                if firstchar.isdigit():
                    one = line.split()[0]
                    rest = " ".join(line.split()[1:])
                    print('<div id="p{}" class="sect"><a href="#a{}">{}</a></div>'.format(one, one, rest), file=html)
                else:
                    if ord(firstchar) < 256:
                        # portuguese
                        print(f'<div class="pt">{line}</div>', file=html)
                    else:
                        print(f'<div class="gr">{line}</div>', file=html)
            else:
                print('<div class="sp">&nbsp;</div>', file=html)
                        

        for line in open("part_appendix.txt", encoding="utf-8"):
            print(line, end="", file=html)

        print("<br><br><br><br><br>", file=html)
