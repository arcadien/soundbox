from flask import Flask, request,make_response
import os

app = Flask("Horn")


textCommand="echo '{}' | espeak -s 110 -v mb/mb-fr1 | mbrola /usr/share/mbrola/{}/{} - - | aplay -r16000 -fS16"

@app.route("/")
def index():

    states = ["success", "failed", "unstable"]
    if "state" in request.args and request.args["state"] in states:
        state = request.args["state"]
        os.system("aplay ./{}.wav".format(state))
    elif "speech" in request.args and "voice" in request.args:
        os.system(textCommand.format(request.args['speech'], request.args['voice'], request.args['voice']))

    response = make_response("""
<!DOCTYPE html>
<html>
    <head />
    <body>
        <form target="/">
            <textarea name="speech" row="4" cols="40">Type text here</textarea>
            <select name="voice">
                <option value="tl1">tl1</option>
                <option value="br2">br2</option>
                <option value="ma1">ma1</option>
                <option value="cz2">cz2</option>
                <option value="nz1">nz1</option>
                <option value="mx2">mx2</option>
                <option value="lt2">lt2</option>
                <option value="en1">en1</option>
                <option value="jp3">jp3</option>
                <option value="hb1">hb1</option>
                <option value="es2">es2</option>
                <option value="it1">it1</option>
                <option value="es1">es1</option>
                <option value="hn1">hn1</option>
                <option value="ic1">ic1</option>
                <option value="ca2">ca2</option>
                <option value="de2">de2</option>
                <option value="it3">it3</option>
                <option value="ar1">ar1</option>
                <option value="gr2">gr2</option>
                <option value="ee1">ee1</option>
                <option value="nl1">nl1</option>
                <option value="de5">de5</option>
                <option value="de6">de6</option>
                <option value="us3">us3</option>
                <option value="de1">de1</option>
                <option value="lt1">lt1</option>
                <option value="us1">us1</option>
                <option value="pt1">pt1</option>
                <option value="es4">es4</option>
                <option value="us2">us2</option>
                <option value="fr4">fr4</option>
                <option value="nl2">nl2</option>
                <option value="cn1">cn1</option>
                <option value="de7">de7</option>
                <option value="fr5">fr5</option>
                <option value="tr2">tr2</option>
                <option value="ca1">ca1</option>
                <option value="gr1">gr1</option>
                <option value="fr3">fr3</option>
                <option value="it2">it2</option>
                <option value="tr1">tr1</option>
                <option value="cr1">cr1</option>
                <option value="fr7">fr7</option>
                <option value="ro1">ro1</option>
                <option value="af1">af1</option>
                <option value="hb2">hb2</option>
                <option value="fr2">fr2</option>
                <option value="id1">id1</option>
                <option value="de3">de3</option>
                <option value="cz1">cz1</option>
                <option value="fr1">fr1</option>
                <option value="sw1">sw1</option>
                <option value="it4">it4</option>
                <option value="jp1">jp1</option>
                <option value="fr6">fr6</option>
                <option value="de8">de8</option>
                <option value="bz1">bz1</option>
                <option value="de4">de4</option>
                <option value="vz1">vz1</option>
                <option value="br1">br1</option>
                <option value="mx1">mx1</option>
                <option value="pl1">pl1</option>
                <option value="sw2">sw2</option>
                <option value="in2">in2</option>
                <option value="ir1">ir1</option>
                <option value="es3">es3</option>
                <option value="br4">br4</option>
                <option value="hu1">hu1</option>
                <option value="in1">in1</option>
                <option value="jp2">jp2</option>
                <option value="ar2">ar2</option>
                <option value="br3">br3</option>
                <option value="la1">la1</option>
                <option value="nl3">nl3</option>
            </select>  
                        <input type="submit"></input>
        </form>
    </body>
</html>
""", 200)

    return response
if __name__ == '__main__':
    app.run(port=4567, host="0.0.0.0")

