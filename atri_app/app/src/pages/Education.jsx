import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Flex as Flex5 } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { Div as Div5 } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { TextBox as TextBox5 } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { Image as Image5 } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { useFlex38Cb, useFlex39Cb, useDiv174Cb, useFlex41Cb, useDiv176Cb, useDiv177Cb, useDiv178Cb, useFlex42Cb, useDiv179Cb, useDiv180Cb, useDiv181Cb, useFlex43Cb, useDiv182Cb, useDiv183Cb, useDiv184Cb, useFlex40Cb, useFlex45Cb, useDiv185Cb, useDiv186Cb, useDiv187Cb, useDiv189Cb, useFlex46Cb, useDiv190Cb, useDiv191Cb, useDiv192Cb, useDiv193Cb, useFlex47Cb, useDiv194Cb, useDiv195Cb, useDiv196Cb, useDiv197Cb, useTextBox194Cb, useTextBox196Cb, useTextBox197Cb, useTextBox198Cb, useImage47Cb, useImage48Cb, useTextBox199Cb, useTextBox200Cb, useTextBox201Cb, useTextBox202Cb, useTextBox203Cb, useTextBox204Cb, useImage49Cb, useTextBox195Cb, useImage50Cb, useTextBox205Cb, useTextBox206Cb, useTextBox207Cb, useImage51Cb, useImage52Cb, useTextBox208Cb, useTextBox209Cb, useTextBox214Cb, useImage53Cb, useImage54Cb, useTextBox211Cb, useTextBox212Cb, useTextBox215Cb, useImage55Cb } from "../page-cbs/education";
import "../page-css/education.css";
import "../custom/education";

export default function Education() {
  const navigate = useNavigate();
  useEffect(() => {
    const unsub = subscribeInternalNavigation((url) => {
      navigate(url);
    });
    return unsub;
  }, [navigate]);

  const location = useLocation();
  useLayoutEffect(()=>{
    fetchPageProps(location.pathname, location.search).then((res)=>{
      updateStoreStateFromController(res.pageName, res.pageState)
    })
  }, [location])

  const Flex38Props = useStore((state)=>state["education"]["Flex38"]);
const Flex38IoProps = useIoStore((state)=>state["education"]["Flex38"]);
const Flex38Cb = useFlex38Cb()
const Flex39Props = useStore((state)=>state["education"]["Flex39"]);
const Flex39IoProps = useIoStore((state)=>state["education"]["Flex39"]);
const Flex39Cb = useFlex39Cb()
const Div174Props = useStore((state)=>state["education"]["Div174"]);
const Div174IoProps = useIoStore((state)=>state["education"]["Div174"]);
const Div174Cb = useDiv174Cb()
const Flex41Props = useStore((state)=>state["education"]["Flex41"]);
const Flex41IoProps = useIoStore((state)=>state["education"]["Flex41"]);
const Flex41Cb = useFlex41Cb()
const Div176Props = useStore((state)=>state["education"]["Div176"]);
const Div176IoProps = useIoStore((state)=>state["education"]["Div176"]);
const Div176Cb = useDiv176Cb()
const Div177Props = useStore((state)=>state["education"]["Div177"]);
const Div177IoProps = useIoStore((state)=>state["education"]["Div177"]);
const Div177Cb = useDiv177Cb()
const Div178Props = useStore((state)=>state["education"]["Div178"]);
const Div178IoProps = useIoStore((state)=>state["education"]["Div178"]);
const Div178Cb = useDiv178Cb()
const Flex42Props = useStore((state)=>state["education"]["Flex42"]);
const Flex42IoProps = useIoStore((state)=>state["education"]["Flex42"]);
const Flex42Cb = useFlex42Cb()
const Div179Props = useStore((state)=>state["education"]["Div179"]);
const Div179IoProps = useIoStore((state)=>state["education"]["Div179"]);
const Div179Cb = useDiv179Cb()
const Div180Props = useStore((state)=>state["education"]["Div180"]);
const Div180IoProps = useIoStore((state)=>state["education"]["Div180"]);
const Div180Cb = useDiv180Cb()
const Div181Props = useStore((state)=>state["education"]["Div181"]);
const Div181IoProps = useIoStore((state)=>state["education"]["Div181"]);
const Div181Cb = useDiv181Cb()
const Flex43Props = useStore((state)=>state["education"]["Flex43"]);
const Flex43IoProps = useIoStore((state)=>state["education"]["Flex43"]);
const Flex43Cb = useFlex43Cb()
const Div182Props = useStore((state)=>state["education"]["Div182"]);
const Div182IoProps = useIoStore((state)=>state["education"]["Div182"]);
const Div182Cb = useDiv182Cb()
const Div183Props = useStore((state)=>state["education"]["Div183"]);
const Div183IoProps = useIoStore((state)=>state["education"]["Div183"]);
const Div183Cb = useDiv183Cb()
const Div184Props = useStore((state)=>state["education"]["Div184"]);
const Div184IoProps = useIoStore((state)=>state["education"]["Div184"]);
const Div184Cb = useDiv184Cb()
const Flex40Props = useStore((state)=>state["education"]["Flex40"]);
const Flex40IoProps = useIoStore((state)=>state["education"]["Flex40"]);
const Flex40Cb = useFlex40Cb()
const Flex45Props = useStore((state)=>state["education"]["Flex45"]);
const Flex45IoProps = useIoStore((state)=>state["education"]["Flex45"]);
const Flex45Cb = useFlex45Cb()
const Div185Props = useStore((state)=>state["education"]["Div185"]);
const Div185IoProps = useIoStore((state)=>state["education"]["Div185"]);
const Div185Cb = useDiv185Cb()
const Div186Props = useStore((state)=>state["education"]["Div186"]);
const Div186IoProps = useIoStore((state)=>state["education"]["Div186"]);
const Div186Cb = useDiv186Cb()
const Div187Props = useStore((state)=>state["education"]["Div187"]);
const Div187IoProps = useIoStore((state)=>state["education"]["Div187"]);
const Div187Cb = useDiv187Cb()
const Div189Props = useStore((state)=>state["education"]["Div189"]);
const Div189IoProps = useIoStore((state)=>state["education"]["Div189"]);
const Div189Cb = useDiv189Cb()
const Flex46Props = useStore((state)=>state["education"]["Flex46"]);
const Flex46IoProps = useIoStore((state)=>state["education"]["Flex46"]);
const Flex46Cb = useFlex46Cb()
const Div190Props = useStore((state)=>state["education"]["Div190"]);
const Div190IoProps = useIoStore((state)=>state["education"]["Div190"]);
const Div190Cb = useDiv190Cb()
const Div191Props = useStore((state)=>state["education"]["Div191"]);
const Div191IoProps = useIoStore((state)=>state["education"]["Div191"]);
const Div191Cb = useDiv191Cb()
const Div192Props = useStore((state)=>state["education"]["Div192"]);
const Div192IoProps = useIoStore((state)=>state["education"]["Div192"]);
const Div192Cb = useDiv192Cb()
const Div193Props = useStore((state)=>state["education"]["Div193"]);
const Div193IoProps = useIoStore((state)=>state["education"]["Div193"]);
const Div193Cb = useDiv193Cb()
const Flex47Props = useStore((state)=>state["education"]["Flex47"]);
const Flex47IoProps = useIoStore((state)=>state["education"]["Flex47"]);
const Flex47Cb = useFlex47Cb()
const Div194Props = useStore((state)=>state["education"]["Div194"]);
const Div194IoProps = useIoStore((state)=>state["education"]["Div194"]);
const Div194Cb = useDiv194Cb()
const Div195Props = useStore((state)=>state["education"]["Div195"]);
const Div195IoProps = useIoStore((state)=>state["education"]["Div195"]);
const Div195Cb = useDiv195Cb()
const Div196Props = useStore((state)=>state["education"]["Div196"]);
const Div196IoProps = useIoStore((state)=>state["education"]["Div196"]);
const Div196Cb = useDiv196Cb()
const Div197Props = useStore((state)=>state["education"]["Div197"]);
const Div197IoProps = useIoStore((state)=>state["education"]["Div197"]);
const Div197Cb = useDiv197Cb()
const TextBox194Props = useStore((state)=>state["education"]["TextBox194"]);
const TextBox194IoProps = useIoStore((state)=>state["education"]["TextBox194"]);
const TextBox194Cb = useTextBox194Cb()
const TextBox196Props = useStore((state)=>state["education"]["TextBox196"]);
const TextBox196IoProps = useIoStore((state)=>state["education"]["TextBox196"]);
const TextBox196Cb = useTextBox196Cb()
const TextBox197Props = useStore((state)=>state["education"]["TextBox197"]);
const TextBox197IoProps = useIoStore((state)=>state["education"]["TextBox197"]);
const TextBox197Cb = useTextBox197Cb()
const TextBox198Props = useStore((state)=>state["education"]["TextBox198"]);
const TextBox198IoProps = useIoStore((state)=>state["education"]["TextBox198"]);
const TextBox198Cb = useTextBox198Cb()
const Image47Props = useStore((state)=>state["education"]["Image47"]);
const Image47IoProps = useIoStore((state)=>state["education"]["Image47"]);
const Image47Cb = useImage47Cb()
const Image48Props = useStore((state)=>state["education"]["Image48"]);
const Image48IoProps = useIoStore((state)=>state["education"]["Image48"]);
const Image48Cb = useImage48Cb()
const TextBox199Props = useStore((state)=>state["education"]["TextBox199"]);
const TextBox199IoProps = useIoStore((state)=>state["education"]["TextBox199"]);
const TextBox199Cb = useTextBox199Cb()
const TextBox200Props = useStore((state)=>state["education"]["TextBox200"]);
const TextBox200IoProps = useIoStore((state)=>state["education"]["TextBox200"]);
const TextBox200Cb = useTextBox200Cb()
const TextBox201Props = useStore((state)=>state["education"]["TextBox201"]);
const TextBox201IoProps = useIoStore((state)=>state["education"]["TextBox201"]);
const TextBox201Cb = useTextBox201Cb()
const TextBox202Props = useStore((state)=>state["education"]["TextBox202"]);
const TextBox202IoProps = useIoStore((state)=>state["education"]["TextBox202"]);
const TextBox202Cb = useTextBox202Cb()
const TextBox203Props = useStore((state)=>state["education"]["TextBox203"]);
const TextBox203IoProps = useIoStore((state)=>state["education"]["TextBox203"]);
const TextBox203Cb = useTextBox203Cb()
const TextBox204Props = useStore((state)=>state["education"]["TextBox204"]);
const TextBox204IoProps = useIoStore((state)=>state["education"]["TextBox204"]);
const TextBox204Cb = useTextBox204Cb()
const Image49Props = useStore((state)=>state["education"]["Image49"]);
const Image49IoProps = useIoStore((state)=>state["education"]["Image49"]);
const Image49Cb = useImage49Cb()
const TextBox195Props = useStore((state)=>state["education"]["TextBox195"]);
const TextBox195IoProps = useIoStore((state)=>state["education"]["TextBox195"]);
const TextBox195Cb = useTextBox195Cb()
const Image50Props = useStore((state)=>state["education"]["Image50"]);
const Image50IoProps = useIoStore((state)=>state["education"]["Image50"]);
const Image50Cb = useImage50Cb()
const TextBox205Props = useStore((state)=>state["education"]["TextBox205"]);
const TextBox205IoProps = useIoStore((state)=>state["education"]["TextBox205"]);
const TextBox205Cb = useTextBox205Cb()
const TextBox206Props = useStore((state)=>state["education"]["TextBox206"]);
const TextBox206IoProps = useIoStore((state)=>state["education"]["TextBox206"]);
const TextBox206Cb = useTextBox206Cb()
const TextBox207Props = useStore((state)=>state["education"]["TextBox207"]);
const TextBox207IoProps = useIoStore((state)=>state["education"]["TextBox207"]);
const TextBox207Cb = useTextBox207Cb()
const Image51Props = useStore((state)=>state["education"]["Image51"]);
const Image51IoProps = useIoStore((state)=>state["education"]["Image51"]);
const Image51Cb = useImage51Cb()
const Image52Props = useStore((state)=>state["education"]["Image52"]);
const Image52IoProps = useIoStore((state)=>state["education"]["Image52"]);
const Image52Cb = useImage52Cb()
const TextBox208Props = useStore((state)=>state["education"]["TextBox208"]);
const TextBox208IoProps = useIoStore((state)=>state["education"]["TextBox208"]);
const TextBox208Cb = useTextBox208Cb()
const TextBox209Props = useStore((state)=>state["education"]["TextBox209"]);
const TextBox209IoProps = useIoStore((state)=>state["education"]["TextBox209"]);
const TextBox209Cb = useTextBox209Cb()
const TextBox214Props = useStore((state)=>state["education"]["TextBox214"]);
const TextBox214IoProps = useIoStore((state)=>state["education"]["TextBox214"]);
const TextBox214Cb = useTextBox214Cb()
const Image53Props = useStore((state)=>state["education"]["Image53"]);
const Image53IoProps = useIoStore((state)=>state["education"]["Image53"]);
const Image53Cb = useImage53Cb()
const Image54Props = useStore((state)=>state["education"]["Image54"]);
const Image54IoProps = useIoStore((state)=>state["education"]["Image54"]);
const Image54Cb = useImage54Cb()
const TextBox211Props = useStore((state)=>state["education"]["TextBox211"]);
const TextBox211IoProps = useIoStore((state)=>state["education"]["TextBox211"]);
const TextBox211Cb = useTextBox211Cb()
const TextBox212Props = useStore((state)=>state["education"]["TextBox212"]);
const TextBox212IoProps = useIoStore((state)=>state["education"]["TextBox212"]);
const TextBox212Cb = useTextBox212Cb()
const TextBox215Props = useStore((state)=>state["education"]["TextBox215"]);
const TextBox215IoProps = useIoStore((state)=>state["education"]["TextBox215"]);
const TextBox215Cb = useTextBox215Cb()
const Image55Props = useStore((state)=>state["education"]["Image55"]);
const Image55IoProps = useIoStore((state)=>state["education"]["Image55"]);
const Image55Cb = useImage55Cb()

  return (<>
  <Flex5 className="p-education Flex38 bpt" {...Flex38Props} {...Flex38Cb} {...Flex38IoProps}>
<Flex5 className="p-education Flex39 bpt" {...Flex39Props} {...Flex39Cb} {...Flex39IoProps}>
<Div5 className="p-education Div174 bpt" {...Div174Props} {...Div174Cb} {...Div174IoProps}>
<TextBox5 className="p-education TextBox194 bpt" {...TextBox194Props} {...TextBox194Cb} {...TextBox194IoProps}/>
</Div5>
<Flex5 className="p-education Flex41 bpt" {...Flex41Props} {...Flex41Cb} {...Flex41IoProps}>
<Div5 className="p-education Div176 bpt" {...Div176Props} {...Div176Cb} {...Div176IoProps}>
<TextBox5 className="p-education TextBox196 bpt" {...TextBox196Props} {...TextBox196Cb} {...TextBox196IoProps}/>
<TextBox5 className="p-education TextBox197 bpt" {...TextBox197Props} {...TextBox197Cb} {...TextBox197IoProps}/>
</Div5>
<Div5 className="p-education Div177 bpt" {...Div177Props} {...Div177Cb} {...Div177IoProps}>
<TextBox5 className="p-education TextBox198 bpt" {...TextBox198Props} {...TextBox198Cb} {...TextBox198IoProps}/>
</Div5>
<Div5 className="p-education Div178 bpt" {...Div178Props} {...Div178Cb} {...Div178IoProps}>
<Image5 className="p-education Image47 bpt" {...Image47Props} {...Image47Cb} {...Image47IoProps}/>
</Div5>
</Flex5>
<Flex5 className="p-education Flex42 bpt" {...Flex42Props} {...Flex42Cb} {...Flex42IoProps}>
<Div5 className="p-education Div181 bpt" {...Div181Props} {...Div181Cb} {...Div181IoProps}>
<TextBox5 className="p-education TextBox201 bpt" {...TextBox201Props} {...TextBox201Cb} {...TextBox201IoProps}/>
<TextBox5 className="p-education TextBox200 bpt" {...TextBox200Props} {...TextBox200Cb} {...TextBox200IoProps}/>
</Div5>
<Div5 className="p-education Div180 bpt" {...Div180Props} {...Div180Cb} {...Div180IoProps}>
<TextBox5 className="p-education TextBox199 bpt" {...TextBox199Props} {...TextBox199Cb} {...TextBox199IoProps}/>
</Div5>
<Div5 className="p-education Div179 bpt" {...Div179Props} {...Div179Cb} {...Div179IoProps}>
<Image5 className="p-education Image48 bpt" {...Image48Props} {...Image48Cb} {...Image48IoProps}/>
</Div5>
</Flex5>
<Flex5 className="p-education Flex43 bpt" {...Flex43Props} {...Flex43Cb} {...Flex43IoProps}>
<Div5 className="p-education Div182 bpt" {...Div182Props} {...Div182Cb} {...Div182IoProps}>
<TextBox5 className="p-education TextBox202 bpt" {...TextBox202Props} {...TextBox202Cb} {...TextBox202IoProps}/>
<TextBox5 className="p-education TextBox203 bpt" {...TextBox203Props} {...TextBox203Cb} {...TextBox203IoProps}/>
</Div5>
<Div5 className="p-education Div183 bpt" {...Div183Props} {...Div183Cb} {...Div183IoProps}>
<TextBox5 className="p-education TextBox204 bpt" {...TextBox204Props} {...TextBox204Cb} {...TextBox204IoProps}/>
</Div5>
<Div5 className="p-education Div184 bpt" {...Div184Props} {...Div184Cb} {...Div184IoProps}>
<Image5 className="p-education Image49 bpt" {...Image49Props} {...Image49Cb} {...Image49IoProps}/>
</Div5>
</Flex5>
</Flex5>
<Flex5 className="p-education Flex40 bpt" {...Flex40Props} {...Flex40Cb} {...Flex40IoProps}>
<TextBox5 className="p-education TextBox195 bpt" {...TextBox195Props} {...TextBox195Cb} {...TextBox195IoProps}/>
<Flex5 className="p-education Flex45 bpt" {...Flex45Props} {...Flex45Cb} {...Flex45IoProps}>
<Div5 className="p-education Div189 bpt" {...Div189Props} {...Div189Cb} {...Div189IoProps}>
<Image5 className="p-education Image51 bpt" {...Image51Props} {...Image51Cb} {...Image51IoProps}/>
</Div5>
<Div5 className="p-education Div187 bpt" {...Div187Props} {...Div187Cb} {...Div187IoProps}>
<TextBox5 className="p-education TextBox207 bpt" {...TextBox207Props} {...TextBox207Cb} {...TextBox207IoProps}/>
<TextBox5 className="p-education TextBox206 bpt" {...TextBox206Props} {...TextBox206Cb} {...TextBox206IoProps}/>
</Div5>
<Div5 className="p-education Div186 bpt" {...Div186Props} {...Div186Cb} {...Div186IoProps}>
<TextBox5 className="p-education TextBox205 bpt" {...TextBox205Props} {...TextBox205Cb} {...TextBox205IoProps}/>
</Div5>
<Div5 className="p-education Div185 bpt" {...Div185Props} {...Div185Cb} {...Div185IoProps}>
<Image5 className="p-education Image50 bpt" {...Image50Props} {...Image50Cb} {...Image50IoProps}/>
</Div5>
</Flex5>
<Flex5 className="p-education Flex46 bpt" {...Flex46Props} {...Flex46Cb} {...Flex46IoProps}>
<Div5 className="p-education Div190 bpt" {...Div190Props} {...Div190Cb} {...Div190IoProps}>
<Image5 className="p-education Image52 bpt" {...Image52Props} {...Image52Cb} {...Image52IoProps}/>
</Div5>
<Div5 className="p-education Div191 bpt" {...Div191Props} {...Div191Cb} {...Div191IoProps}>
<TextBox5 className="p-education TextBox208 bpt" {...TextBox208Props} {...TextBox208Cb} {...TextBox208IoProps}/>
<TextBox5 className="p-education TextBox209 bpt" {...TextBox209Props} {...TextBox209Cb} {...TextBox209IoProps}/>
</Div5>
<Div5 className="p-education Div192 bpt" {...Div192Props} {...Div192Cb} {...Div192IoProps}>
<TextBox5 className="p-education TextBox214 bpt" {...TextBox214Props} {...TextBox214Cb} {...TextBox214IoProps}/>
</Div5>
<Div5 className="p-education Div193 bpt" {...Div193Props} {...Div193Cb} {...Div193IoProps}>
<Image5 className="p-education Image53 bpt" {...Image53Props} {...Image53Cb} {...Image53IoProps}/>
</Div5>
</Flex5>
<Flex5 className="p-education Flex47 bpt" {...Flex47Props} {...Flex47Cb} {...Flex47IoProps}>
<Div5 className="p-education Div194 bpt" {...Div194Props} {...Div194Cb} {...Div194IoProps}>
<Image5 className="p-education Image54 bpt" {...Image54Props} {...Image54Cb} {...Image54IoProps}/>
</Div5>
<Div5 className="p-education Div195 bpt" {...Div195Props} {...Div195Cb} {...Div195IoProps}>
<TextBox5 className="p-education TextBox211 bpt" {...TextBox211Props} {...TextBox211Cb} {...TextBox211IoProps}/>
<TextBox5 className="p-education TextBox212 bpt" {...TextBox212Props} {...TextBox212Cb} {...TextBox212IoProps}/>
</Div5>
<Div5 className="p-education Div196 bpt" {...Div196Props} {...Div196Cb} {...Div196IoProps}>
<TextBox5 className="p-education TextBox215 bpt" {...TextBox215Props} {...TextBox215Cb} {...TextBox215IoProps}/>
</Div5>
<Div5 className="p-education Div197 bpt" {...Div197Props} {...Div197Cb} {...Div197IoProps}>
<Image5 className="p-education Image55 bpt" {...Image55Props} {...Image55Cb} {...Image55IoProps}/>
</Div5>
</Flex5>
</Flex5>
</Flex5>
  </>);
}
