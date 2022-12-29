import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Div as Div2 } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { Flex as Flex2 } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { Image as Image2 } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { TextBox as TextBox2 } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { Button as Button1 } from "@atrilabs/react-component-manifests/src/manifests/Button/Button.tsx";
import { useDiv313Cb, useFlex86Cb, useFlex87Cb, useDiv326Cb, useFlex88Cb, useDiv319Cb, useFlex89Cb, useDiv321Cb, useDiv314Cb, useDiv322Cb, useDiv315Cb, useDiv323Cb, useDiv316Cb, useDiv324Cb, useDiv317Cb, useDiv325Cb, useDiv318Cb, useImage88Cb, useTextBox358Cb, useTextBox359Cb, useTextBox360Cb, useTextBox361Cb, useTextBox362Cb, useImage89Cb, useDiv320Cb, useButton14Cb, useTextBox363Cb, useTextBox364Cb, useTextBox365Cb, useTextBox366Cb, useTextBox367Cb, useTextBox368Cb, useImage90Cb, useTextBox369Cb, useTextBox370Cb, useTextBox371Cb, useImage91Cb, useTextBox372Cb, useTextBox373Cb, useTextBox374Cb, useImage92Cb, useTextBox375Cb, useTextBox376Cb, useTextBox377Cb, useImage93Cb, useTextBox378Cb, useTextBox379Cb, useTextBox380Cb, useImage94Cb } from "../page-cbs/projects";
import "../page-css/projects.css";
import "../custom/projects";

export default function Projects() {
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

  const Div313Props = useStore((state)=>state["projects"]["Div313"]);
const Div313IoProps = useIoStore((state)=>state["projects"]["Div313"]);
const Div313Cb = useDiv313Cb()
const Flex86Props = useStore((state)=>state["projects"]["Flex86"]);
const Flex86IoProps = useIoStore((state)=>state["projects"]["Flex86"]);
const Flex86Cb = useFlex86Cb()
const Flex87Props = useStore((state)=>state["projects"]["Flex87"]);
const Flex87IoProps = useIoStore((state)=>state["projects"]["Flex87"]);
const Flex87Cb = useFlex87Cb()
const Div326Props = useStore((state)=>state["projects"]["Div326"]);
const Div326IoProps = useIoStore((state)=>state["projects"]["Div326"]);
const Div326Cb = useDiv326Cb()
const Flex88Props = useStore((state)=>state["projects"]["Flex88"]);
const Flex88IoProps = useIoStore((state)=>state["projects"]["Flex88"]);
const Flex88Cb = useFlex88Cb()
const Div319Props = useStore((state)=>state["projects"]["Div319"]);
const Div319IoProps = useIoStore((state)=>state["projects"]["Div319"]);
const Div319Cb = useDiv319Cb()
const Flex89Props = useStore((state)=>state["projects"]["Flex89"]);
const Flex89IoProps = useIoStore((state)=>state["projects"]["Flex89"]);
const Flex89Cb = useFlex89Cb()
const Div321Props = useStore((state)=>state["projects"]["Div321"]);
const Div321IoProps = useIoStore((state)=>state["projects"]["Div321"]);
const Div321Cb = useDiv321Cb()
const Div314Props = useStore((state)=>state["projects"]["Div314"]);
const Div314IoProps = useIoStore((state)=>state["projects"]["Div314"]);
const Div314Cb = useDiv314Cb()
const Div322Props = useStore((state)=>state["projects"]["Div322"]);
const Div322IoProps = useIoStore((state)=>state["projects"]["Div322"]);
const Div322Cb = useDiv322Cb()
const Div315Props = useStore((state)=>state["projects"]["Div315"]);
const Div315IoProps = useIoStore((state)=>state["projects"]["Div315"]);
const Div315Cb = useDiv315Cb()
const Div323Props = useStore((state)=>state["projects"]["Div323"]);
const Div323IoProps = useIoStore((state)=>state["projects"]["Div323"]);
const Div323Cb = useDiv323Cb()
const Div316Props = useStore((state)=>state["projects"]["Div316"]);
const Div316IoProps = useIoStore((state)=>state["projects"]["Div316"]);
const Div316Cb = useDiv316Cb()
const Div324Props = useStore((state)=>state["projects"]["Div324"]);
const Div324IoProps = useIoStore((state)=>state["projects"]["Div324"]);
const Div324Cb = useDiv324Cb()
const Div317Props = useStore((state)=>state["projects"]["Div317"]);
const Div317IoProps = useIoStore((state)=>state["projects"]["Div317"]);
const Div317Cb = useDiv317Cb()
const Div325Props = useStore((state)=>state["projects"]["Div325"]);
const Div325IoProps = useIoStore((state)=>state["projects"]["Div325"]);
const Div325Cb = useDiv325Cb()
const Div318Props = useStore((state)=>state["projects"]["Div318"]);
const Div318IoProps = useIoStore((state)=>state["projects"]["Div318"]);
const Div318Cb = useDiv318Cb()
const Image88Props = useStore((state)=>state["projects"]["Image88"]);
const Image88IoProps = useIoStore((state)=>state["projects"]["Image88"]);
const Image88Cb = useImage88Cb()
const TextBox358Props = useStore((state)=>state["projects"]["TextBox358"]);
const TextBox358IoProps = useIoStore((state)=>state["projects"]["TextBox358"]);
const TextBox358Cb = useTextBox358Cb()
const TextBox359Props = useStore((state)=>state["projects"]["TextBox359"]);
const TextBox359IoProps = useIoStore((state)=>state["projects"]["TextBox359"]);
const TextBox359Cb = useTextBox359Cb()
const TextBox360Props = useStore((state)=>state["projects"]["TextBox360"]);
const TextBox360IoProps = useIoStore((state)=>state["projects"]["TextBox360"]);
const TextBox360Cb = useTextBox360Cb()
const TextBox361Props = useStore((state)=>state["projects"]["TextBox361"]);
const TextBox361IoProps = useIoStore((state)=>state["projects"]["TextBox361"]);
const TextBox361Cb = useTextBox361Cb()
const TextBox362Props = useStore((state)=>state["projects"]["TextBox362"]);
const TextBox362IoProps = useIoStore((state)=>state["projects"]["TextBox362"]);
const TextBox362Cb = useTextBox362Cb()
const Image89Props = useStore((state)=>state["projects"]["Image89"]);
const Image89IoProps = useIoStore((state)=>state["projects"]["Image89"]);
const Image89Cb = useImage89Cb()
const Div320Props = useStore((state)=>state["projects"]["Div320"]);
const Div320IoProps = useIoStore((state)=>state["projects"]["Div320"]);
const Div320Cb = useDiv320Cb()
const Button14Props = useStore((state)=>state["projects"]["Button14"]);
const Button14IoProps = useIoStore((state)=>state["projects"]["Button14"]);
const Button14Cb = useButton14Cb()
const TextBox363Props = useStore((state)=>state["projects"]["TextBox363"]);
const TextBox363IoProps = useIoStore((state)=>state["projects"]["TextBox363"]);
const TextBox363Cb = useTextBox363Cb()
const TextBox364Props = useStore((state)=>state["projects"]["TextBox364"]);
const TextBox364IoProps = useIoStore((state)=>state["projects"]["TextBox364"]);
const TextBox364Cb = useTextBox364Cb()
const TextBox365Props = useStore((state)=>state["projects"]["TextBox365"]);
const TextBox365IoProps = useIoStore((state)=>state["projects"]["TextBox365"]);
const TextBox365Cb = useTextBox365Cb()
const TextBox366Props = useStore((state)=>state["projects"]["TextBox366"]);
const TextBox366IoProps = useIoStore((state)=>state["projects"]["TextBox366"]);
const TextBox366Cb = useTextBox366Cb()
const TextBox367Props = useStore((state)=>state["projects"]["TextBox367"]);
const TextBox367IoProps = useIoStore((state)=>state["projects"]["TextBox367"]);
const TextBox367Cb = useTextBox367Cb()
const TextBox368Props = useStore((state)=>state["projects"]["TextBox368"]);
const TextBox368IoProps = useIoStore((state)=>state["projects"]["TextBox368"]);
const TextBox368Cb = useTextBox368Cb()
const Image90Props = useStore((state)=>state["projects"]["Image90"]);
const Image90IoProps = useIoStore((state)=>state["projects"]["Image90"]);
const Image90Cb = useImage90Cb()
const TextBox369Props = useStore((state)=>state["projects"]["TextBox369"]);
const TextBox369IoProps = useIoStore((state)=>state["projects"]["TextBox369"]);
const TextBox369Cb = useTextBox369Cb()
const TextBox370Props = useStore((state)=>state["projects"]["TextBox370"]);
const TextBox370IoProps = useIoStore((state)=>state["projects"]["TextBox370"]);
const TextBox370Cb = useTextBox370Cb()
const TextBox371Props = useStore((state)=>state["projects"]["TextBox371"]);
const TextBox371IoProps = useIoStore((state)=>state["projects"]["TextBox371"]);
const TextBox371Cb = useTextBox371Cb()
const Image91Props = useStore((state)=>state["projects"]["Image91"]);
const Image91IoProps = useIoStore((state)=>state["projects"]["Image91"]);
const Image91Cb = useImage91Cb()
const TextBox372Props = useStore((state)=>state["projects"]["TextBox372"]);
const TextBox372IoProps = useIoStore((state)=>state["projects"]["TextBox372"]);
const TextBox372Cb = useTextBox372Cb()
const TextBox373Props = useStore((state)=>state["projects"]["TextBox373"]);
const TextBox373IoProps = useIoStore((state)=>state["projects"]["TextBox373"]);
const TextBox373Cb = useTextBox373Cb()
const TextBox374Props = useStore((state)=>state["projects"]["TextBox374"]);
const TextBox374IoProps = useIoStore((state)=>state["projects"]["TextBox374"]);
const TextBox374Cb = useTextBox374Cb()
const Image92Props = useStore((state)=>state["projects"]["Image92"]);
const Image92IoProps = useIoStore((state)=>state["projects"]["Image92"]);
const Image92Cb = useImage92Cb()
const TextBox375Props = useStore((state)=>state["projects"]["TextBox375"]);
const TextBox375IoProps = useIoStore((state)=>state["projects"]["TextBox375"]);
const TextBox375Cb = useTextBox375Cb()
const TextBox376Props = useStore((state)=>state["projects"]["TextBox376"]);
const TextBox376IoProps = useIoStore((state)=>state["projects"]["TextBox376"]);
const TextBox376Cb = useTextBox376Cb()
const TextBox377Props = useStore((state)=>state["projects"]["TextBox377"]);
const TextBox377IoProps = useIoStore((state)=>state["projects"]["TextBox377"]);
const TextBox377Cb = useTextBox377Cb()
const Image93Props = useStore((state)=>state["projects"]["Image93"]);
const Image93IoProps = useIoStore((state)=>state["projects"]["Image93"]);
const Image93Cb = useImage93Cb()
const TextBox378Props = useStore((state)=>state["projects"]["TextBox378"]);
const TextBox378IoProps = useIoStore((state)=>state["projects"]["TextBox378"]);
const TextBox378Cb = useTextBox378Cb()
const TextBox379Props = useStore((state)=>state["projects"]["TextBox379"]);
const TextBox379IoProps = useIoStore((state)=>state["projects"]["TextBox379"]);
const TextBox379Cb = useTextBox379Cb()
const TextBox380Props = useStore((state)=>state["projects"]["TextBox380"]);
const TextBox380IoProps = useIoStore((state)=>state["projects"]["TextBox380"]);
const TextBox380Cb = useTextBox380Cb()
const Image94Props = useStore((state)=>state["projects"]["Image94"]);
const Image94IoProps = useIoStore((state)=>state["projects"]["Image94"]);
const Image94Cb = useImage94Cb()

  return (<>
  <Div2 className="p-projects Div313 bpt" {...Div313Props} {...Div313Cb} {...Div313IoProps}>
<Flex2 className="p-projects Flex86 bpt" {...Flex86Props} {...Flex86Cb} {...Flex86IoProps}>
<TextBox2 className="p-projects TextBox362 bpt" {...TextBox362Props} {...TextBox362Cb} {...TextBox362IoProps}/>
<TextBox2 className="p-projects TextBox361 bpt" {...TextBox361Props} {...TextBox361Cb} {...TextBox361IoProps}/>
<TextBox2 className="p-projects TextBox360 bpt" {...TextBox360Props} {...TextBox360Cb} {...TextBox360IoProps}/>
<TextBox2 className="p-projects TextBox359 bpt" {...TextBox359Props} {...TextBox359Cb} {...TextBox359IoProps}/>
<TextBox2 className="p-projects TextBox358 bpt" {...TextBox358Props} {...TextBox358Cb} {...TextBox358IoProps}/>
<Image2 className="p-projects Image88 bpt" {...Image88Props} {...Image88Cb} {...Image88IoProps}/>
</Flex2>
<Flex2 className="p-projects Flex87 bpt" {...Flex87Props} {...Flex87Cb} {...Flex87IoProps}>
<Image2 className="p-projects Image89 bpt" {...Image89Props} {...Image89Cb} {...Image89IoProps}/>
</Flex2>
</Div2>
<Div2 className="p-projects Div326 bpt" {...Div326Props} {...Div326Cb} {...Div326IoProps}>
<Flex2 className="p-projects Flex88 bpt" {...Flex88Props} {...Flex88Cb} {...Flex88IoProps}>
<Div2 className="p-projects Div319 bpt" {...Div319Props} {...Div319Cb} {...Div319IoProps}>
<TextBox2 className="p-projects TextBox363 bpt" {...TextBox363Props} {...TextBox363Cb} {...TextBox363IoProps}/>
<TextBox2 className="p-projects TextBox364 bpt" {...TextBox364Props} {...TextBox364Cb} {...TextBox364IoProps}/>
<TextBox2 className="p-projects TextBox365 bpt" {...TextBox365Props} {...TextBox365Cb} {...TextBox365IoProps}/>
</Div2>
<Button1 className="p-projects Button14 bpt" {...Button14Props} {...Button14Cb} {...Button14IoProps}/>
<Div2 className="p-projects Div320 bpt" {...Div320Props} {...Div320Cb} {...Div320IoProps}/>
</Flex2>
<Flex2 className="p-projects Flex89 bpt" {...Flex89Props} {...Flex89Cb} {...Flex89IoProps}>
<Div2 className="p-projects Div323 bpt" {...Div323Props} {...Div323Cb} {...Div323IoProps}>
<Div2 className="p-projects Div316 bpt" {...Div316Props} {...Div316Cb} {...Div316IoProps}>
<Image2 className="p-projects Image92 bpt" {...Image92Props} {...Image92Cb} {...Image92IoProps}/>
</Div2>
<TextBox2 className="p-projects TextBox374 bpt" {...TextBox374Props} {...TextBox374Cb} {...TextBox374IoProps}/>
<TextBox2 className="p-projects TextBox373 bpt" {...TextBox373Props} {...TextBox373Cb} {...TextBox373IoProps}/>
<TextBox2 className="p-projects TextBox372 bpt" {...TextBox372Props} {...TextBox372Cb} {...TextBox372IoProps}/>
</Div2>
<Div2 className="p-projects Div322 bpt" {...Div322Props} {...Div322Cb} {...Div322IoProps}>
<Div2 className="p-projects Div315 bpt" {...Div315Props} {...Div315Cb} {...Div315IoProps}>
<Image2 className="p-projects Image91 bpt" {...Image91Props} {...Image91Cb} {...Image91IoProps}/>
</Div2>
<TextBox2 className="p-projects TextBox371 bpt" {...TextBox371Props} {...TextBox371Cb} {...TextBox371IoProps}/>
<TextBox2 className="p-projects TextBox370 bpt" {...TextBox370Props} {...TextBox370Cb} {...TextBox370IoProps}/>
<TextBox2 className="p-projects TextBox369 bpt" {...TextBox369Props} {...TextBox369Cb} {...TextBox369IoProps}/>
</Div2>
<Div2 className="p-projects Div321 bpt" {...Div321Props} {...Div321Cb} {...Div321IoProps}>
<Div2 className="p-projects Div314 bpt" {...Div314Props} {...Div314Cb} {...Div314IoProps}>
<Image2 className="p-projects Image90 bpt" {...Image90Props} {...Image90Cb} {...Image90IoProps}/>
</Div2>
<TextBox2 className="p-projects TextBox366 bpt" {...TextBox366Props} {...TextBox366Cb} {...TextBox366IoProps}/>
<TextBox2 className="p-projects TextBox367 bpt" {...TextBox367Props} {...TextBox367Cb} {...TextBox367IoProps}/>
<TextBox2 className="p-projects TextBox368 bpt" {...TextBox368Props} {...TextBox368Cb} {...TextBox368IoProps}/>
</Div2>
<Div2 className="p-projects Div324 bpt" {...Div324Props} {...Div324Cb} {...Div324IoProps}>
<Div2 className="p-projects Div317 bpt" {...Div317Props} {...Div317Cb} {...Div317IoProps}>
<Image2 className="p-projects Image93 bpt" {...Image93Props} {...Image93Cb} {...Image93IoProps}/>
</Div2>
<TextBox2 className="p-projects TextBox377 bpt" {...TextBox377Props} {...TextBox377Cb} {...TextBox377IoProps}/>
<TextBox2 className="p-projects TextBox376 bpt" {...TextBox376Props} {...TextBox376Cb} {...TextBox376IoProps}/>
<TextBox2 className="p-projects TextBox375 bpt" {...TextBox375Props} {...TextBox375Cb} {...TextBox375IoProps}/>
</Div2>
<Div2 className="p-projects Div325 bpt" {...Div325Props} {...Div325Cb} {...Div325IoProps}>
<Div2 className="p-projects Div318 bpt" {...Div318Props} {...Div318Cb} {...Div318IoProps}>
<Image2 className="p-projects Image94 bpt" {...Image94Props} {...Image94Cb} {...Image94IoProps}/>
</Div2>
<TextBox2 className="p-projects TextBox378 bpt" {...TextBox378Props} {...TextBox378Cb} {...TextBox378IoProps}/>
<TextBox2 className="p-projects TextBox379 bpt" {...TextBox379Props} {...TextBox379Cb} {...TextBox379IoProps}/>
<TextBox2 className="p-projects TextBox380 bpt" {...TextBox380Props} {...TextBox380Cb} {...TextBox380IoProps}/>
</Div2>
</Flex2>
</Div2>
  </>);
}
