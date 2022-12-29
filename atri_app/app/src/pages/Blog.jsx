import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Div as Div3 } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { Flex as Flex3 } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { Image as Image3 } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { TextBox as TextBox3 } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { useDiv327Cb, useFlex90Cb, useFlex91Cb, useDiv336Cb, useFlex95Cb, useDiv343Cb, useDiv344Cb, useFlex94Cb, useDiv337Cb, useDiv338Cb, useDiv339Cb, useDiv340Cb, useDiv341Cb, useDiv342Cb, useImage95Cb, useTextBox381Cb, useTextBox382Cb, useTextBox383Cb, useTextBox384Cb, useTextBox385Cb, useImage96Cb, useTextBox425Cb, useTextBox426Cb, useTextBox427Cb, useTextBox407Cb, useTextBox408Cb, useTextBox409Cb, useTextBox410Cb, useTextBox411Cb, useTextBox412Cb, useTextBox413Cb, useTextBox414Cb, useTextBox415Cb, useTextBox416Cb, useTextBox417Cb, useTextBox418Cb, useTextBox419Cb, useTextBox420Cb, useTextBox421Cb, useTextBox422Cb, useTextBox423Cb, useTextBox424Cb } from "../page-cbs/blog";
import "../page-css/blog.css";
import "../custom/blog";

export default function Blog() {
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

  const Div327Props = useStore((state)=>state["blog"]["Div327"]);
const Div327IoProps = useIoStore((state)=>state["blog"]["Div327"]);
const Div327Cb = useDiv327Cb()
const Flex90Props = useStore((state)=>state["blog"]["Flex90"]);
const Flex90IoProps = useIoStore((state)=>state["blog"]["Flex90"]);
const Flex90Cb = useFlex90Cb()
const Flex91Props = useStore((state)=>state["blog"]["Flex91"]);
const Flex91IoProps = useIoStore((state)=>state["blog"]["Flex91"]);
const Flex91Cb = useFlex91Cb()
const Div336Props = useStore((state)=>state["blog"]["Div336"]);
const Div336IoProps = useIoStore((state)=>state["blog"]["Div336"]);
const Div336Cb = useDiv336Cb()
const Flex95Props = useStore((state)=>state["blog"]["Flex95"]);
const Flex95IoProps = useIoStore((state)=>state["blog"]["Flex95"]);
const Flex95Cb = useFlex95Cb()
const Div343Props = useStore((state)=>state["blog"]["Div343"]);
const Div343IoProps = useIoStore((state)=>state["blog"]["Div343"]);
const Div343Cb = useDiv343Cb()
const Div344Props = useStore((state)=>state["blog"]["Div344"]);
const Div344IoProps = useIoStore((state)=>state["blog"]["Div344"]);
const Div344Cb = useDiv344Cb()
const Flex94Props = useStore((state)=>state["blog"]["Flex94"]);
const Flex94IoProps = useIoStore((state)=>state["blog"]["Flex94"]);
const Flex94Cb = useFlex94Cb()
const Div337Props = useStore((state)=>state["blog"]["Div337"]);
const Div337IoProps = useIoStore((state)=>state["blog"]["Div337"]);
const Div337Cb = useDiv337Cb()
const Div338Props = useStore((state)=>state["blog"]["Div338"]);
const Div338IoProps = useIoStore((state)=>state["blog"]["Div338"]);
const Div338Cb = useDiv338Cb()
const Div339Props = useStore((state)=>state["blog"]["Div339"]);
const Div339IoProps = useIoStore((state)=>state["blog"]["Div339"]);
const Div339Cb = useDiv339Cb()
const Div340Props = useStore((state)=>state["blog"]["Div340"]);
const Div340IoProps = useIoStore((state)=>state["blog"]["Div340"]);
const Div340Cb = useDiv340Cb()
const Div341Props = useStore((state)=>state["blog"]["Div341"]);
const Div341IoProps = useIoStore((state)=>state["blog"]["Div341"]);
const Div341Cb = useDiv341Cb()
const Div342Props = useStore((state)=>state["blog"]["Div342"]);
const Div342IoProps = useIoStore((state)=>state["blog"]["Div342"]);
const Div342Cb = useDiv342Cb()
const Image95Props = useStore((state)=>state["blog"]["Image95"]);
const Image95IoProps = useIoStore((state)=>state["blog"]["Image95"]);
const Image95Cb = useImage95Cb()
const TextBox381Props = useStore((state)=>state["blog"]["TextBox381"]);
const TextBox381IoProps = useIoStore((state)=>state["blog"]["TextBox381"]);
const TextBox381Cb = useTextBox381Cb()
const TextBox382Props = useStore((state)=>state["blog"]["TextBox382"]);
const TextBox382IoProps = useIoStore((state)=>state["blog"]["TextBox382"]);
const TextBox382Cb = useTextBox382Cb()
const TextBox383Props = useStore((state)=>state["blog"]["TextBox383"]);
const TextBox383IoProps = useIoStore((state)=>state["blog"]["TextBox383"]);
const TextBox383Cb = useTextBox383Cb()
const TextBox384Props = useStore((state)=>state["blog"]["TextBox384"]);
const TextBox384IoProps = useIoStore((state)=>state["blog"]["TextBox384"]);
const TextBox384Cb = useTextBox384Cb()
const TextBox385Props = useStore((state)=>state["blog"]["TextBox385"]);
const TextBox385IoProps = useIoStore((state)=>state["blog"]["TextBox385"]);
const TextBox385Cb = useTextBox385Cb()
const Image96Props = useStore((state)=>state["blog"]["Image96"]);
const Image96IoProps = useIoStore((state)=>state["blog"]["Image96"]);
const Image96Cb = useImage96Cb()
const TextBox425Props = useStore((state)=>state["blog"]["TextBox425"]);
const TextBox425IoProps = useIoStore((state)=>state["blog"]["TextBox425"]);
const TextBox425Cb = useTextBox425Cb()
const TextBox426Props = useStore((state)=>state["blog"]["TextBox426"]);
const TextBox426IoProps = useIoStore((state)=>state["blog"]["TextBox426"]);
const TextBox426Cb = useTextBox426Cb()
const TextBox427Props = useStore((state)=>state["blog"]["TextBox427"]);
const TextBox427IoProps = useIoStore((state)=>state["blog"]["TextBox427"]);
const TextBox427Cb = useTextBox427Cb()
const TextBox407Props = useStore((state)=>state["blog"]["TextBox407"]);
const TextBox407IoProps = useIoStore((state)=>state["blog"]["TextBox407"]);
const TextBox407Cb = useTextBox407Cb()
const TextBox408Props = useStore((state)=>state["blog"]["TextBox408"]);
const TextBox408IoProps = useIoStore((state)=>state["blog"]["TextBox408"]);
const TextBox408Cb = useTextBox408Cb()
const TextBox409Props = useStore((state)=>state["blog"]["TextBox409"]);
const TextBox409IoProps = useIoStore((state)=>state["blog"]["TextBox409"]);
const TextBox409Cb = useTextBox409Cb()
const TextBox410Props = useStore((state)=>state["blog"]["TextBox410"]);
const TextBox410IoProps = useIoStore((state)=>state["blog"]["TextBox410"]);
const TextBox410Cb = useTextBox410Cb()
const TextBox411Props = useStore((state)=>state["blog"]["TextBox411"]);
const TextBox411IoProps = useIoStore((state)=>state["blog"]["TextBox411"]);
const TextBox411Cb = useTextBox411Cb()
const TextBox412Props = useStore((state)=>state["blog"]["TextBox412"]);
const TextBox412IoProps = useIoStore((state)=>state["blog"]["TextBox412"]);
const TextBox412Cb = useTextBox412Cb()
const TextBox413Props = useStore((state)=>state["blog"]["TextBox413"]);
const TextBox413IoProps = useIoStore((state)=>state["blog"]["TextBox413"]);
const TextBox413Cb = useTextBox413Cb()
const TextBox414Props = useStore((state)=>state["blog"]["TextBox414"]);
const TextBox414IoProps = useIoStore((state)=>state["blog"]["TextBox414"]);
const TextBox414Cb = useTextBox414Cb()
const TextBox415Props = useStore((state)=>state["blog"]["TextBox415"]);
const TextBox415IoProps = useIoStore((state)=>state["blog"]["TextBox415"]);
const TextBox415Cb = useTextBox415Cb()
const TextBox416Props = useStore((state)=>state["blog"]["TextBox416"]);
const TextBox416IoProps = useIoStore((state)=>state["blog"]["TextBox416"]);
const TextBox416Cb = useTextBox416Cb()
const TextBox417Props = useStore((state)=>state["blog"]["TextBox417"]);
const TextBox417IoProps = useIoStore((state)=>state["blog"]["TextBox417"]);
const TextBox417Cb = useTextBox417Cb()
const TextBox418Props = useStore((state)=>state["blog"]["TextBox418"]);
const TextBox418IoProps = useIoStore((state)=>state["blog"]["TextBox418"]);
const TextBox418Cb = useTextBox418Cb()
const TextBox419Props = useStore((state)=>state["blog"]["TextBox419"]);
const TextBox419IoProps = useIoStore((state)=>state["blog"]["TextBox419"]);
const TextBox419Cb = useTextBox419Cb()
const TextBox420Props = useStore((state)=>state["blog"]["TextBox420"]);
const TextBox420IoProps = useIoStore((state)=>state["blog"]["TextBox420"]);
const TextBox420Cb = useTextBox420Cb()
const TextBox421Props = useStore((state)=>state["blog"]["TextBox421"]);
const TextBox421IoProps = useIoStore((state)=>state["blog"]["TextBox421"]);
const TextBox421Cb = useTextBox421Cb()
const TextBox422Props = useStore((state)=>state["blog"]["TextBox422"]);
const TextBox422IoProps = useIoStore((state)=>state["blog"]["TextBox422"]);
const TextBox422Cb = useTextBox422Cb()
const TextBox423Props = useStore((state)=>state["blog"]["TextBox423"]);
const TextBox423IoProps = useIoStore((state)=>state["blog"]["TextBox423"]);
const TextBox423Cb = useTextBox423Cb()
const TextBox424Props = useStore((state)=>state["blog"]["TextBox424"]);
const TextBox424IoProps = useIoStore((state)=>state["blog"]["TextBox424"]);
const TextBox424Cb = useTextBox424Cb()

  return (<>
  <Div3 className="p-blog Div327 bpt" {...Div327Props} {...Div327Cb} {...Div327IoProps}>
<Flex3 className="p-blog Flex90 bpt" {...Flex90Props} {...Flex90Cb} {...Flex90IoProps}>
<TextBox3 className="p-blog TextBox385 bpt" {...TextBox385Props} {...TextBox385Cb} {...TextBox385IoProps}/>
<TextBox3 className="p-blog TextBox384 bpt" {...TextBox384Props} {...TextBox384Cb} {...TextBox384IoProps}/>
<TextBox3 className="p-blog TextBox383 bpt" {...TextBox383Props} {...TextBox383Cb} {...TextBox383IoProps}/>
<TextBox3 className="p-blog TextBox382 bpt" {...TextBox382Props} {...TextBox382Cb} {...TextBox382IoProps}/>
<TextBox3 className="p-blog TextBox381 bpt" {...TextBox381Props} {...TextBox381Cb} {...TextBox381IoProps}/>
<Image3 className="p-blog Image95 bpt" {...Image95Props} {...Image95Cb} {...Image95IoProps}/>
</Flex3>
<Flex3 className="p-blog Flex91 bpt" {...Flex91Props} {...Flex91Cb} {...Flex91IoProps}>
<Image3 className="p-blog Image96 bpt" {...Image96Props} {...Image96Cb} {...Image96IoProps}/>
</Flex3>
</Div3>
<Div3 className="p-blog Div336 bpt" {...Div336Props} {...Div336Cb} {...Div336IoProps}>
<Flex3 className="p-blog Flex95 bpt" {...Flex95Props} {...Flex95Cb} {...Flex95IoProps}>
<Div3 className="p-blog Div343 bpt" {...Div343Props} {...Div343Cb} {...Div343IoProps}>
<TextBox3 className="p-blog TextBox425 bpt" {...TextBox425Props} {...TextBox425Cb} {...TextBox425IoProps}/>
<TextBox3 className="p-blog TextBox426 bpt" {...TextBox426Props} {...TextBox426Cb} {...TextBox426IoProps}/>
<TextBox3 className="p-blog TextBox427 bpt" {...TextBox427Props} {...TextBox427Cb} {...TextBox427IoProps}/>
</Div3>
<Div3 className="p-blog Div344 bpt" {...Div344Props} {...Div344Cb} {...Div344IoProps}>
<Flex3 className="p-blog Flex94 bpt" {...Flex94Props} {...Flex94Cb} {...Flex94IoProps}>
<Div3 className="p-blog Div337 bpt" {...Div337Props} {...Div337Cb} {...Div337IoProps}>
<TextBox3 className="p-blog TextBox408 bpt" {...TextBox408Props} {...TextBox408Cb} {...TextBox408IoProps}/>
<TextBox3 className="p-blog TextBox407 bpt" {...TextBox407Props} {...TextBox407Cb} {...TextBox407IoProps}/>
<TextBox3 className="p-blog TextBox409 bpt" {...TextBox409Props} {...TextBox409Cb} {...TextBox409IoProps}/>
</Div3>
<Div3 className="p-blog Div339 bpt" {...Div339Props} {...Div339Cb} {...Div339IoProps}>
<TextBox3 className="p-blog TextBox414 bpt" {...TextBox414Props} {...TextBox414Cb} {...TextBox414IoProps}/>
<TextBox3 className="p-blog TextBox413 bpt" {...TextBox413Props} {...TextBox413Cb} {...TextBox413IoProps}/>
<TextBox3 className="p-blog TextBox415 bpt" {...TextBox415Props} {...TextBox415Cb} {...TextBox415IoProps}/>
</Div3>
<Div3 className="p-blog Div338 bpt" {...Div338Props} {...Div338Cb} {...Div338IoProps}>
<TextBox3 className="p-blog TextBox411 bpt" {...TextBox411Props} {...TextBox411Cb} {...TextBox411IoProps}/>
<TextBox3 className="p-blog TextBox410 bpt" {...TextBox410Props} {...TextBox410Cb} {...TextBox410IoProps}/>
<TextBox3 className="p-blog TextBox412 bpt" {...TextBox412Props} {...TextBox412Cb} {...TextBox412IoProps}/>
</Div3>
<Div3 className="p-blog Div340 bpt" {...Div340Props} {...Div340Cb} {...Div340IoProps}>
<TextBox3 className="p-blog TextBox417 bpt" {...TextBox417Props} {...TextBox417Cb} {...TextBox417IoProps}/>
<TextBox3 className="p-blog TextBox418 bpt" {...TextBox418Props} {...TextBox418Cb} {...TextBox418IoProps}/>
<TextBox3 className="p-blog TextBox416 bpt" {...TextBox416Props} {...TextBox416Cb} {...TextBox416IoProps}/>
</Div3>
<Div3 className="p-blog Div341 bpt" {...Div341Props} {...Div341Cb} {...Div341IoProps}>
<TextBox3 className="p-blog TextBox420 bpt" {...TextBox420Props} {...TextBox420Cb} {...TextBox420IoProps}/>
<TextBox3 className="p-blog TextBox419 bpt" {...TextBox419Props} {...TextBox419Cb} {...TextBox419IoProps}/>
<TextBox3 className="p-blog TextBox421 bpt" {...TextBox421Props} {...TextBox421Cb} {...TextBox421IoProps}/>
</Div3>
<Div3 className="p-blog Div342 bpt" {...Div342Props} {...Div342Cb} {...Div342IoProps}>
<TextBox3 className="p-blog TextBox423 bpt" {...TextBox423Props} {...TextBox423Cb} {...TextBox423IoProps}/>
<TextBox3 className="p-blog TextBox424 bpt" {...TextBox424Props} {...TextBox424Cb} {...TextBox424IoProps}/>
<TextBox3 className="p-blog TextBox422 bpt" {...TextBox422Props} {...TextBox422Cb} {...TextBox422IoProps}/>
</Div3>
</Flex3>
</Div3>
</Flex3>
</Div3>
  </>);
}
