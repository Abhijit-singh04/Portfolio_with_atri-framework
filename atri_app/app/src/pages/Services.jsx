import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Div as Div1 } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { Flex as Flex1 } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { Image as Image1 } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { TextBox as TextBox1 } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { useDiv308Cb, useFlex83Cb, useFlex84Cb, useDiv312Cb, useFlex85Cb, useDiv309Cb, useDiv310Cb, useDiv311Cb, useImage83Cb, useTextBox335Cb, useTextBox336Cb, useTextBox337Cb, useTextBox338Cb, useTextBox339Cb, useImage84Cb, useTextBox355Cb, useTextBox356Cb, useTextBox357Cb, useImage85Cb, useTextBox340Cb, useTextBox341Cb, useTextBox342Cb, useTextBox343Cb, useTextBox344Cb, useImage86Cb, useTextBox345Cb, useTextBox346Cb, useTextBox347Cb, useTextBox348Cb, useTextBox349Cb, useTextBox350Cb, useTextBox351Cb, useTextBox352Cb, useTextBox353Cb, useTextBox354Cb, useImage87Cb } from "../page-cbs/Services";
import "../page-css/Services.css";
import "../custom/Services";

export default function Services() {
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

  const Div308Props = useStore((state)=>state["Services"]["Div308"]);
const Div308IoProps = useIoStore((state)=>state["Services"]["Div308"]);
const Div308Cb = useDiv308Cb()
const Flex83Props = useStore((state)=>state["Services"]["Flex83"]);
const Flex83IoProps = useIoStore((state)=>state["Services"]["Flex83"]);
const Flex83Cb = useFlex83Cb()
const Flex84Props = useStore((state)=>state["Services"]["Flex84"]);
const Flex84IoProps = useIoStore((state)=>state["Services"]["Flex84"]);
const Flex84Cb = useFlex84Cb()
const Div312Props = useStore((state)=>state["Services"]["Div312"]);
const Div312IoProps = useIoStore((state)=>state["Services"]["Div312"]);
const Div312Cb = useDiv312Cb()
const Flex85Props = useStore((state)=>state["Services"]["Flex85"]);
const Flex85IoProps = useIoStore((state)=>state["Services"]["Flex85"]);
const Flex85Cb = useFlex85Cb()
const Div309Props = useStore((state)=>state["Services"]["Div309"]);
const Div309IoProps = useIoStore((state)=>state["Services"]["Div309"]);
const Div309Cb = useDiv309Cb()
const Div310Props = useStore((state)=>state["Services"]["Div310"]);
const Div310IoProps = useIoStore((state)=>state["Services"]["Div310"]);
const Div310Cb = useDiv310Cb()
const Div311Props = useStore((state)=>state["Services"]["Div311"]);
const Div311IoProps = useIoStore((state)=>state["Services"]["Div311"]);
const Div311Cb = useDiv311Cb()
const Image83Props = useStore((state)=>state["Services"]["Image83"]);
const Image83IoProps = useIoStore((state)=>state["Services"]["Image83"]);
const Image83Cb = useImage83Cb()
const TextBox335Props = useStore((state)=>state["Services"]["TextBox335"]);
const TextBox335IoProps = useIoStore((state)=>state["Services"]["TextBox335"]);
const TextBox335Cb = useTextBox335Cb()
const TextBox336Props = useStore((state)=>state["Services"]["TextBox336"]);
const TextBox336IoProps = useIoStore((state)=>state["Services"]["TextBox336"]);
const TextBox336Cb = useTextBox336Cb()
const TextBox337Props = useStore((state)=>state["Services"]["TextBox337"]);
const TextBox337IoProps = useIoStore((state)=>state["Services"]["TextBox337"]);
const TextBox337Cb = useTextBox337Cb()
const TextBox338Props = useStore((state)=>state["Services"]["TextBox338"]);
const TextBox338IoProps = useIoStore((state)=>state["Services"]["TextBox338"]);
const TextBox338Cb = useTextBox338Cb()
const TextBox339Props = useStore((state)=>state["Services"]["TextBox339"]);
const TextBox339IoProps = useIoStore((state)=>state["Services"]["TextBox339"]);
const TextBox339Cb = useTextBox339Cb()
const Image84Props = useStore((state)=>state["Services"]["Image84"]);
const Image84IoProps = useIoStore((state)=>state["Services"]["Image84"]);
const Image84Cb = useImage84Cb()
const TextBox355Props = useStore((state)=>state["Services"]["TextBox355"]);
const TextBox355IoProps = useIoStore((state)=>state["Services"]["TextBox355"]);
const TextBox355Cb = useTextBox355Cb()
const TextBox356Props = useStore((state)=>state["Services"]["TextBox356"]);
const TextBox356IoProps = useIoStore((state)=>state["Services"]["TextBox356"]);
const TextBox356Cb = useTextBox356Cb()
const TextBox357Props = useStore((state)=>state["Services"]["TextBox357"]);
const TextBox357IoProps = useIoStore((state)=>state["Services"]["TextBox357"]);
const TextBox357Cb = useTextBox357Cb()
const Image85Props = useStore((state)=>state["Services"]["Image85"]);
const Image85IoProps = useIoStore((state)=>state["Services"]["Image85"]);
const Image85Cb = useImage85Cb()
const TextBox340Props = useStore((state)=>state["Services"]["TextBox340"]);
const TextBox340IoProps = useIoStore((state)=>state["Services"]["TextBox340"]);
const TextBox340Cb = useTextBox340Cb()
const TextBox341Props = useStore((state)=>state["Services"]["TextBox341"]);
const TextBox341IoProps = useIoStore((state)=>state["Services"]["TextBox341"]);
const TextBox341Cb = useTextBox341Cb()
const TextBox342Props = useStore((state)=>state["Services"]["TextBox342"]);
const TextBox342IoProps = useIoStore((state)=>state["Services"]["TextBox342"]);
const TextBox342Cb = useTextBox342Cb()
const TextBox343Props = useStore((state)=>state["Services"]["TextBox343"]);
const TextBox343IoProps = useIoStore((state)=>state["Services"]["TextBox343"]);
const TextBox343Cb = useTextBox343Cb()
const TextBox344Props = useStore((state)=>state["Services"]["TextBox344"]);
const TextBox344IoProps = useIoStore((state)=>state["Services"]["TextBox344"]);
const TextBox344Cb = useTextBox344Cb()
const Image86Props = useStore((state)=>state["Services"]["Image86"]);
const Image86IoProps = useIoStore((state)=>state["Services"]["Image86"]);
const Image86Cb = useImage86Cb()
const TextBox345Props = useStore((state)=>state["Services"]["TextBox345"]);
const TextBox345IoProps = useIoStore((state)=>state["Services"]["TextBox345"]);
const TextBox345Cb = useTextBox345Cb()
const TextBox346Props = useStore((state)=>state["Services"]["TextBox346"]);
const TextBox346IoProps = useIoStore((state)=>state["Services"]["TextBox346"]);
const TextBox346Cb = useTextBox346Cb()
const TextBox347Props = useStore((state)=>state["Services"]["TextBox347"]);
const TextBox347IoProps = useIoStore((state)=>state["Services"]["TextBox347"]);
const TextBox347Cb = useTextBox347Cb()
const TextBox348Props = useStore((state)=>state["Services"]["TextBox348"]);
const TextBox348IoProps = useIoStore((state)=>state["Services"]["TextBox348"]);
const TextBox348Cb = useTextBox348Cb()
const TextBox349Props = useStore((state)=>state["Services"]["TextBox349"]);
const TextBox349IoProps = useIoStore((state)=>state["Services"]["TextBox349"]);
const TextBox349Cb = useTextBox349Cb()
const TextBox350Props = useStore((state)=>state["Services"]["TextBox350"]);
const TextBox350IoProps = useIoStore((state)=>state["Services"]["TextBox350"]);
const TextBox350Cb = useTextBox350Cb()
const TextBox351Props = useStore((state)=>state["Services"]["TextBox351"]);
const TextBox351IoProps = useIoStore((state)=>state["Services"]["TextBox351"]);
const TextBox351Cb = useTextBox351Cb()
const TextBox352Props = useStore((state)=>state["Services"]["TextBox352"]);
const TextBox352IoProps = useIoStore((state)=>state["Services"]["TextBox352"]);
const TextBox352Cb = useTextBox352Cb()
const TextBox353Props = useStore((state)=>state["Services"]["TextBox353"]);
const TextBox353IoProps = useIoStore((state)=>state["Services"]["TextBox353"]);
const TextBox353Cb = useTextBox353Cb()
const TextBox354Props = useStore((state)=>state["Services"]["TextBox354"]);
const TextBox354IoProps = useIoStore((state)=>state["Services"]["TextBox354"]);
const TextBox354Cb = useTextBox354Cb()
const Image87Props = useStore((state)=>state["Services"]["Image87"]);
const Image87IoProps = useIoStore((state)=>state["Services"]["Image87"]);
const Image87Cb = useImage87Cb()

  return (<>
  <Div1 className="p-Services Div308 bpt" {...Div308Props} {...Div308Cb} {...Div308IoProps}>
<Flex1 className="p-Services Flex83 bpt" {...Flex83Props} {...Flex83Cb} {...Flex83IoProps}>
<TextBox1 className="p-Services TextBox339 bpt" {...TextBox339Props} {...TextBox339Cb} {...TextBox339IoProps}/>
<TextBox1 className="p-Services TextBox338 bpt" {...TextBox338Props} {...TextBox338Cb} {...TextBox338IoProps}/>
<TextBox1 className="p-Services TextBox337 bpt" {...TextBox337Props} {...TextBox337Cb} {...TextBox337IoProps}/>
<TextBox1 className="p-Services TextBox336 bpt" {...TextBox336Props} {...TextBox336Cb} {...TextBox336IoProps}/>
<TextBox1 className="p-Services TextBox335 bpt" {...TextBox335Props} {...TextBox335Cb} {...TextBox335IoProps}/>
<Image1 className="p-Services Image83 bpt" {...Image83Props} {...Image83Cb} {...Image83IoProps}/>
</Flex1>
<Flex1 className="p-Services Flex84 bpt" {...Flex84Props} {...Flex84Cb} {...Flex84IoProps}>
<Image1 className="p-Services Image84 bpt" {...Image84Props} {...Image84Cb} {...Image84IoProps}/>
</Flex1>
</Div1>
<Div1 className="p-Services Div312 bpt" {...Div312Props} {...Div312Cb} {...Div312IoProps}>
<TextBox1 className="p-Services TextBox357 bpt" {...TextBox357Props} {...TextBox357Cb} {...TextBox357IoProps}/>
<TextBox1 className="p-Services TextBox356 bpt" {...TextBox356Props} {...TextBox356Cb} {...TextBox356IoProps}/>
<TextBox1 className="p-Services TextBox355 bpt" {...TextBox355Props} {...TextBox355Cb} {...TextBox355IoProps}/>
<Flex1 className="p-Services Flex85 bpt" {...Flex85Props} {...Flex85Cb} {...Flex85IoProps}>
<Div1 className="p-Services Div311 bpt" {...Div311Props} {...Div311Cb} {...Div311IoProps}>
<Image1 className="p-Services Image87 bpt" {...Image87Props} {...Image87Cb} {...Image87IoProps}/>
<TextBox1 className="p-Services TextBox350 bpt" {...TextBox350Props} {...TextBox350Cb} {...TextBox350IoProps}/>
<TextBox1 className="p-Services TextBox351 bpt" {...TextBox351Props} {...TextBox351Cb} {...TextBox351IoProps}/>
<TextBox1 className="p-Services TextBox352 bpt" {...TextBox352Props} {...TextBox352Cb} {...TextBox352IoProps}/>
<TextBox1 className="p-Services TextBox353 bpt" {...TextBox353Props} {...TextBox353Cb} {...TextBox353IoProps}/>
<TextBox1 className="p-Services TextBox354 bpt" {...TextBox354Props} {...TextBox354Cb} {...TextBox354IoProps}/>
</Div1>
<Div1 className="p-Services Div309 bpt" {...Div309Props} {...Div309Cb} {...Div309IoProps}>
<Image1 className="p-Services Image85 bpt" {...Image85Props} {...Image85Cb} {...Image85IoProps}/>
<TextBox1 className="p-Services TextBox344 bpt" {...TextBox344Props} {...TextBox344Cb} {...TextBox344IoProps}/>
<TextBox1 className="p-Services TextBox343 bpt" {...TextBox343Props} {...TextBox343Cb} {...TextBox343IoProps}/>
<TextBox1 className="p-Services TextBox342 bpt" {...TextBox342Props} {...TextBox342Cb} {...TextBox342IoProps}/>
<TextBox1 className="p-Services TextBox341 bpt" {...TextBox341Props} {...TextBox341Cb} {...TextBox341IoProps}/>
<TextBox1 className="p-Services TextBox340 bpt" {...TextBox340Props} {...TextBox340Cb} {...TextBox340IoProps}/>
</Div1>
<Div1 className="p-Services Div310 bpt" {...Div310Props} {...Div310Cb} {...Div310IoProps}>
<Image1 className="p-Services Image86 bpt" {...Image86Props} {...Image86Cb} {...Image86IoProps}/>
<TextBox1 className="p-Services TextBox349 bpt" {...TextBox349Props} {...TextBox349Cb} {...TextBox349IoProps}/>
<TextBox1 className="p-Services TextBox348 bpt" {...TextBox348Props} {...TextBox348Cb} {...TextBox348IoProps}/>
<TextBox1 className="p-Services TextBox347 bpt" {...TextBox347Props} {...TextBox347Cb} {...TextBox347IoProps}/>
<TextBox1 className="p-Services TextBox346 bpt" {...TextBox346Props} {...TextBox346Cb} {...TextBox346IoProps}/>
<TextBox1 className="p-Services TextBox345 bpt" {...TextBox345Props} {...TextBox345Cb} {...TextBox345IoProps}/>
</Div1>
</Flex1>
</Div1>
  </>);
}
