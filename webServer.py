from flask import Flask, request,make_response
import os

app = Flask("Horn")


#textCommand="echo \"{}\" | espeak -s 110 | mbrola /usr/share/mbrola/{}/{} - - | aplay -r16000 -fS16"
textCommand="echo \"{}\" | espeak -v {} -s 110"

@app.route("/")
def index():

    states = ["success", "failed", "unstable"]
    if "state" in request.args and request.args["state"] in states:
        state = request.args["state"]
        os.system("aplay ./{}.wav".format(state))
    elif "speech" in request.args and "vocable" in request.args:
        os.system(textCommand.format( request.args['speech'], request.args['vocable']))

    response = make_response("""
<!DOCTYPE html>
<html>
    <head>
    <script type="text/javascript">
    function sortSelect(selElem) {
      var tmpAry = new Array();
      for (var i=0;i<selElem.options.length;i++) {
        tmpAry[i] = new Array();
        tmpAry[i][0] = selElem.options[i].text;
        tmpAry[i][1] = selElem.options[i].value;
      }
      tmpAry.sort();
      while (selElem.options.length > 0) {
        selElem.options[0] = null;
      }
      for (var i=0;i<tmpAry.length;i++) {
        var op = new Option(tmpAry[i][0], tmpAry[i][1]);
        selElem.options[i] = op;
      }
      return;
    }
    </script>
    </head>
    <body>
        <form target="/">
            <select name="state">
                <option value="success">succeeded</option>
                <option value="failed">failed</option>
                <option value="unstable">unstable</option>
            </select>
            <input type="submit" value="!! SAMPLE !!" />
        </form>
        <form target="/">
            <textarea name="speech" row="4" cols="40">Type text here</textarea>
            <select name="vocable">
                <option value="mb/mb-fr1" selected="selected">Français</option>
                <option value="mb/mb-fr4">Français (molasson)</option>
                <option value="mb/mb-nl2-en">Anglais</option>
                <option value="mb/mb-us2">Anglais US</option>
                <option value="europe/nl">Hollandais</option>
                <!--
                <option value="asia/ne">asia/ne</option>
                <option value="asia/fa">asia/fa</option>
                <option value="asia/id">asia/id</option>
                <option value="asia/ka">asia/ka</option>
                <option value="asia/gu">asia/gu</option>
                <option value="asia/fa-pin">asia/fa-pin</option>
                <option value="asia/fa-en-us">asia/fa-en-us</option>
                <option value="asia/hy">asia/hy</option>
                <option value="asia/hy-west">asia/hy-west</option>
                <option value="asia/zh">asia/zh</option>
                <option value="asia/tr">asia/tr</option>
                <option value="asia/bn">asia/bn</option>
                <option value="asia/pa">asia/pa</option>
                <option value="asia/hi">asia/hi</option>
                <option value="asia/ta">asia/ta</option>
                <option value="asia/ku">asia/ku</option>
                <option value="asia/vi">asia/vi</option>
                <option value="asia/kn">asia/kn</option>
                <option value="asia/ml">asia/ml</option>
                <option value="asia/te">asia/te</option>
                <option value="asia/ms">asia/ms</option>
                <option value="asia/zh-yue">asia/zh-yue</option>
                <option value="asia/vi-hue">asia/vi-hue</option>
                <option value="asia/vi-sgn">asia/vi-sgn</option>
                <option value="es-la">es-la</option>
                <option value="europe/eu">europe/eu</option>
                <option value="europe/mk">europe/mk</option>
                <option value="europe/sv">europe/sv</option>
                <option value="europe/is">europe/is</option>
                <option value="europe/fi">europe/fi</option>
                <option value="europe/et">europe/et</option>
                <option value="europe/bg">europe/bg</option>
                <option value="europe/lv">europe/lv</option>
                <option value="europe/it">europe/it</option>
                <option value="europe/no">europe/no</option>
                <option value="europe/es">europe/es</option>
                <option value="europe/fr-be">europe/fr-be</option>
                <option value="europe/sr">europe/sr</option>
                <option value="europe/da">europe/da</option>
                <option value="europe/ga">europe/ga</option>
                <option value="europe/el">europe/el</option>
                <option value="europe/pl">europe/pl</option>
                <option value="europe/lt">europe/lt</option>
                <option value="europe/sk">europe/sk</option>
                <option value="europe/ro">europe/ro</option>
                <option value="europe/pt-pt">europe/pt-pt</option>
                <option value="europe/cs">europe/cs</option>
                <option value="europe/ca">europe/ca</option>
                <option value="europe/cy">europe/cy</option>
                <option value="europe/hr">europe/hr</option>
                <option value="europe/an">europe/an</option>
                <option value="europe/ru">europe/ru</option>
                <option value="europe/bs">europe/bs</option>
                <option value="europe/hu">europe/hu</option>
                <option value="europe/sq">europe/sq</option>
                <option value="en">en</option>
                <option value="default">default</option>
                <option value="pt">pt</option>
                <option value="mb/mb-de7">mb/mb-de7</option>
                <option value="mb/mb-id1">mb/mb-id1</option>
                <option value="mb/mb-ir1">mb/mb-ir1</option>
                <option value="mb/mb-nl2">mb/mb-nl2</option>
                <option value="mb/mb-mx1">mb/mb-mx1</option>
                <option value="mb/mb-fr1-en">mb/mb-fr1-en</option>
                <option value="mb/mb-us1">mb/mb-us1</option>
                <option value="mb/mb-sw2">mb/mb-sw2</option>
                <option value="mb/mb-la1">mb/mb-la1</option>
                <option value="mb/mb-sw2-en">mb/mb-sw2-en</option>
                <option value="mb/mb-es1">mb/mb-es1</option>
                <option value="mb/mb-de5-en">mb/mb-de5-en</option>
                <option value="mb/mb-cz2">mb/mb-cz2</option>
                <option value="mb/mb-ic1">mb/mb-ic1</option>
                <option value="mb/mb-af1-en">mb/mb-af1-en</option>
                <option value="mb/mb-pl1-en">mb/mb-pl1-en</option>
                <option value="mb/mb-es2">mb/mb-es2</option>
                <option value="mb/mb-vz1">mb/mb-vz1</option>
                <option value="mb/mb-ee1">mb/mb-ee1</option>
                <option value="mb/mb-sw1-en">mb/mb-sw1-en</option>
                <option value="mb/mb-de4-en">mb/mb-de4-en</option>
                <option value="mb/mb-gr2">mb/mb-gr2</option>
                <option value="mb/mb-tr2">mb/mb-tr2</option>
                <option value="mb/mb-fr1" selected="selected">mb/mb-fr1</option>
                <option value="mb/mb-en1">mb/mb-en1</option>
                <option value="mb/mb-ro1-en">mb/mb-ro1-en</option>
                <option value="mb/mb-af1">mb/mb-af1</option>
                <option value="mb/mb-de5">mb/mb-de5</option>
                <option value="mb/mb-de6">mb/mb-de6</option>
                <option value="mb/mb-mx2">mb/mb-mx2</option>
                <option value="mb/mb-ro1">mb/mb-ro1</option>
                <option value="mb/mb-hu1-en">mb/mb-hu1-en</option>
                <option value="mb/mb-ir2">mb/mb-ir2</option>
                <option value="mb/mb-br4">mb/mb-br4</option>
                <option value="mb/mb-cr1">mb/mb-cr1</option>
                <option value="mb/mb-sw1">mb/mb-sw1</option>
                <option value="mb/mb-tr1">mb/mb-tr1</option>
                <option value="mb/mb-de6-grc">mb/mb-de6-grc</option>
                <option value="mb/mb-de4">mb/mb-de4</option>
                <option value="mb/mb-br3">mb/mb-br3</option>
                <option value="mb/mb-us3">mb/mb-us3</option>
                <option value="mb/mb-gr2-en">mb/mb-gr2-en</option>
                <option value="mb/mb-fr4-en">mb/mb-fr4-en</option>
                <option value="mb/mb-hu1">mb/mb-hu1</option>
                <option value="mb/mb-pt1">mb/mb-pt1</option>
                <option value="mb/mb-de3">mb/mb-de3</option>
                <option value="mb/mb-it3">mb/mb-it3</option>
                <option value="mb/mb-de2">mb/mb-de2</option>
                <option value="mb/mb-pl1">mb/mb-pl1</option>
                <option value="mb/mb-it4">mb/mb-it4</option>
                <option value="mb/mb-br1">mb/mb-br1</option>
                <option value="other/af">other/af</option>
                <option value="other/lfn">other/lfn</option>
                <option value="other/en-rp">other/en-rp</option>
                <option value="other/sw">other/sw</option>
                <option value="other/eo">other/eo</option>
                <option value="other/en-wi">other/en-wi</option>
                <option value="other/en-n">other/en-n</option>
                <option value="other/en-wm">other/en-wm</option>
                <option value="other/jbo">other/jbo</option>
                <option value="other/en-sc">other/en-sc</option>
                <option value="other/la">other/la</option>
                <option value="other/grc">other/grc</option>
                <option value="other/ia">other/ia</option>
                <option value="fr">fr</option>
                <option value="test/gd">test/gd</option>
                <option value="test/as">test/as</option>
                <option value="test/mr">test/mr</option>
                <option value="test/am">test/am</option>
                <option value="test/kl">test/kl</option>
                <option value="test/si">test/si</option>
                <option value="test/or">test/or</option>
                <option value="test/pap">test/pap</option>
                <option value="test/az">test/az</option>
                <option value="test/ur">test/ur</option>
                <option value="test/sl">test/sl</option>
                <option value="test/nci">test/nci</option>
                <option value="test/ko">test/ko</option>
                <option value="de">de</option>
                <option value="en-us">en-us</option>
                <option value="!v/m7">!v/m7</option>
                <option value="!v/m5">!v/m5</option>
                <option value="!v/f1">!v/f1</option>
                <option value="!v/f5">!v/f5</option>
                <option value="!v/m1">!v/m1</option>
                <option value="!v/klatt">!v/klatt</option>
                <option value="!v/f2">!v/f2</option>
                <option value="!v/m6">!v/m6</option>
                <option value="!v/klatt4">!v/klatt4</option>
                <option value="!v/f3">!v/f3</option>
                <option value="!v/m3">!v/m3</option>
                <option value="!v/m4">!v/m4</option>
                <option value="!v/croak">!v/croak</option>
                <option value="!v/whisper">!v/whisper</option>
                <option value="!v/f4">!v/f4</option>
                <option value="!v/m2">!v/m2</option>
                <option value="!v/whisperf">!v/whisperf</option>
                <option value="!v/klatt3">!v/klatt3</option>
                <option value="!v/klatt2">!v/klatt2</option>
                -->
            </select>
            <input type="submit"></input>
        </form>
    </body>
</html>
""", 200)

    return response
if __name__ == '__main__':
    app.run(port=4567, host="0.0.0.0")

