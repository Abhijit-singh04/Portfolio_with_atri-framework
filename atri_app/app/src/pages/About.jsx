import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Div as Div4 } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { Flex as Flex4 } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { TextBox as TextBox4 } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { Image as Image4 } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { useDiv307Cb, useDiv147Cb, useFlex28Cb, useDiv148Cb, useDiv149Cb, useFlex29Cb, useDiv150Cb, useDiv151Cb, useFlex30Cb, useDiv153Cb, useDiv156Cb, useFlex81Cb, useFlex82Cb, useTextBox185Cb, useTextBox186Cb, useTextBox187Cb, useImage35Cb, useImage36Cb, useImage38Cb, useImage37Cb, useImage81Cb, useTextBox330Cb, useTextBox331Cb, useTextBox332Cb, useTextBox333Cb, useTextBox334Cb, useImage82Cb } from "../page-cbs/About";
import "../page-css/About.css";
import "../custom/About";

export default function About() {
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

  const Div307Props = useStore((state)=>state["About"]["Div307"]);
const Div307IoProps = useIoStore((state)=>state["About"]["Div307"]);
const Div307Cb = useDiv307Cb()
const Div147Props = useStore((state)=>state["About"]["Div147"]);
const Div147IoProps = useIoStore((state)=>state["About"]["Div147"]);
const Div147Cb = useDiv147Cb()
const Flex28Props = useStore((state)=>state["About"]["Flex28"]);
const Flex28IoProps = useIoStore((state)=>state["About"]["Flex28"]);
const Flex28Cb = useFlex28Cb()
const Div148Props = useStore((state)=>state["About"]["Div148"]);
const Div148IoProps = useIoStore((state)=>state["About"]["Div148"]);
const Div148Cb = useDiv148Cb()
const Div149Props = useStore((state)=>state["About"]["Div149"]);
const Div149IoProps = useIoStore((state)=>state["About"]["Div149"]);
const Div149Cb = useDiv149Cb()
const Flex29Props = useStore((state)=>state["About"]["Flex29"]);
const Flex29IoProps = useIoStore((state)=>state["About"]["Flex29"]);
const Flex29Cb = useFlex29Cb()
const Div150Props = useStore((state)=>state["About"]["Div150"]);
const Div150IoProps = useIoStore((state)=>state["About"]["Div150"]);
const Div150Cb = useDiv150Cb()
const Div151Props = useStore((state)=>state["About"]["Div151"]);
const Div151IoProps = useIoStore((state)=>state["About"]["Div151"]);
const Div151Cb = useDiv151Cb()
const Flex30Props = useStore((state)=>state["About"]["Flex30"]);
const Flex30IoProps = useIoStore((state)=>state["About"]["Flex30"]);
const Flex30Cb = useFlex30Cb()
const Div153Props = useStore((state)=>state["About"]["Div153"]);
const Div153IoProps = useIoStore((state)=>state["About"]["Div153"]);
const Div153Cb = useDiv153Cb()
const Div156Props = useStore((state)=>state["About"]["Div156"]);
const Div156IoProps = useIoStore((state)=>state["About"]["Div156"]);
const Div156Cb = useDiv156Cb()
const Flex81Props = useStore((state)=>state["About"]["Flex81"]);
const Flex81IoProps = useIoStore((state)=>state["About"]["Flex81"]);
const Flex81Cb = useFlex81Cb()
const Flex82Props = useStore((state)=>state["About"]["Flex82"]);
const Flex82IoProps = useIoStore((state)=>state["About"]["Flex82"]);
const Flex82Cb = useFlex82Cb()
const TextBox185Props = useStore((state)=>state["About"]["TextBox185"]);
const TextBox185IoProps = useIoStore((state)=>state["About"]["TextBox185"]);
const TextBox185Cb = useTextBox185Cb()
const TextBox186Props = useStore((state)=>state["About"]["TextBox186"]);
const TextBox186IoProps = useIoStore((state)=>state["About"]["TextBox186"]);
const TextBox186Cb = useTextBox186Cb()
const TextBox187Props = useStore((state)=>state["About"]["TextBox187"]);
const TextBox187IoProps = useIoStore((state)=>state["About"]["TextBox187"]);
const TextBox187Cb = useTextBox187Cb()
const Image35Props = useStore((state)=>state["About"]["Image35"]);
const Image35IoProps = useIoStore((state)=>state["About"]["Image35"]);
const Image35Cb = useImage35Cb()
const Image36Props = useStore((state)=>state["About"]["Image36"]);
const Image36IoProps = useIoStore((state)=>state["About"]["Image36"]);
const Image36Cb = useImage36Cb()
const Image38Props = useStore((state)=>state["About"]["Image38"]);
const Image38IoProps = useIoStore((state)=>state["About"]["Image38"]);
const Image38Cb = useImage38Cb()
const Image37Props = useStore((state)=>state["About"]["Image37"]);
const Image37IoProps = useIoStore((state)=>state["About"]["Image37"]);
const Image37Cb = useImage37Cb()
const Image81Props = useStore((state)=>state["About"]["Image81"]);
const Image81IoProps = useIoStore((state)=>state["About"]["Image81"]);
const Image81Cb = useImage81Cb()
const TextBox330Props = useStore((state)=>state["About"]["TextBox330"]);
const TextBox330IoProps = useIoStore((state)=>state["About"]["TextBox330"]);
const TextBox330Cb = useTextBox330Cb()
const TextBox331Props = useStore((state)=>state["About"]["TextBox331"]);
const TextBox331IoProps = useIoStore((state)=>state["About"]["TextBox331"]);
const TextBox331Cb = useTextBox331Cb()
const TextBox332Props = useStore((state)=>state["About"]["TextBox332"]);
const TextBox332IoProps = useIoStore((state)=>state["About"]["TextBox332"]);
const TextBox332Cb = useTextBox332Cb()
const TextBox333Props = useStore((state)=>state["About"]["TextBox333"]);
const TextBox333IoProps = useIoStore((state)=>state["About"]["TextBox333"]);
const TextBox333Cb = useTextBox333Cb()
const TextBox334Props = useStore((state)=>state["About"]["TextBox334"]);
const TextBox334IoProps = useIoStore((state)=>state["About"]["TextBox334"]);
const TextBox334Cb = useTextBox334Cb()
const Image82Props = useStore((state)=>state["About"]["Image82"]);
const Image82IoProps = useIoStore((state)=>state["About"]["Image82"]);
const Image82Cb = useImage82Cb()

  return (<>
  <Div4 className="p-About Div307 bpt" {...Div307Props} {...Div307Cb} {...Div307IoProps}>
<Flex4 className="p-About Flex81 bpt" {...Flex81Props} {...Flex81Cb} {...Flex81IoProps}>
<TextBox4 className="p-About TextBox334 bpt" {...TextBox334Props} {...TextBox334Cb} {...TextBox334IoProps}/>
<TextBox4 className="p-About TextBox333 bpt" {...TextBox333Props} {...TextBox333Cb} {...TextBox333IoProps}/>
<TextBox4 className="p-About TextBox332 bpt" {...TextBox332Props} {...TextBox332Cb} {...TextBox332IoProps}/>
<TextBox4 className="p-About TextBox331 bpt" {...TextBox331Props} {...TextBox331Cb} {...TextBox331IoProps}/>
<TextBox4 className="p-About TextBox330 bpt" {...TextBox330Props} {...TextBox330Cb} {...TextBox330IoProps}/>
<Image4 className="p-About Image81 bpt" {...Image81Props} {...Image81Cb} {...Image81IoProps}/>
</Flex4>
<Flex4 className="p-About Flex82 bpt" {...Flex82Props} {...Flex82Cb} {...Flex82IoProps}>
<Image4 className="p-About Image82 bpt" {...Image82Props} {...Image82Cb} {...Image82IoProps}/>
</Flex4>
<Div4 className="p-About Div147 bpt" {...Div147Props} {...Div147Cb} {...Div147IoProps}>
<Flex4 className="p-About Flex28 bpt" {...Flex28Props} {...Flex28Cb} {...Flex28IoProps}>
<Div4 className="p-About Div148 bpt" {...Div148Props} {...Div148Cb} {...Div148IoProps}>
<TextBox4 className="p-About TextBox185 bpt" {...TextBox185Props} {...TextBox185Cb} {...TextBox185IoProps}/>
<TextBox4 className="p-About TextBox186 bpt" {...TextBox186Props} {...TextBox186Cb} {...TextBox186IoProps}/>
</Div4>
<Div4 className="p-About Div149 bpt" {...Div149Props} {...Div149Cb} {...Div149IoProps}>
<TextBox4 className="p-About TextBox187 bpt" {...TextBox187Props} {...TextBox187Cb} {...TextBox187IoProps}/>
</Div4>
</Flex4>
<Flex4 className="p-About Flex29 bpt" {...Flex29Props} {...Flex29Cb} {...Flex29IoProps}>
<Div4 className="p-About Div150 bpt" {...Div150Props} {...Div150Cb} {...Div150IoProps}>
<Image4 className="p-About Image35 bpt" {...Image35Props} {...Image35Cb} {...Image35IoProps}/>
</Div4>
<Div4 className="p-About Div151 bpt" {...Div151Props} {...Div151Cb} {...Div151IoProps}>
<Image4 className="p-About Image36 bpt" {...Image36Props} {...Image36Cb} {...Image36IoProps}/>
</Div4>
<Flex4 className="p-About Flex30 bpt" {...Flex30Props} {...Flex30Cb} {...Flex30IoProps}>
<Div4 className="p-About Div156 bpt" {...Div156Props} {...Div156Cb} {...Div156IoProps}>
<Image4 className="p-About Image37 bpt" {...Image37Props} {...Image37Cb} {...Image37IoProps}/>
</Div4>
<Div4 className="p-About Div153 bpt" {...Div153Props} {...Div153Cb} {...Div153IoProps}>
<Image4 className="p-About Image38 bpt" {...Image38Props} {...Image38Cb} {...Image38IoProps}/>
</Div4>
</Flex4>
</Flex4>
</Div4>
</Div4>
  </>);
}
