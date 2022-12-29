import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"Div307":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div147":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex28":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div148":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div149":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex29":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div150":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div151":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex30":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div153":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div156":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex81":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex82":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"TextBox185":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox186":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox187":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image35":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image36":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image38":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image37":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image81":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox330":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox331":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox332":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox333":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox334":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image82":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.Div307 = state["Div307"]
		self.Div147 = state["Div147"]
		self.Flex28 = state["Flex28"]
		self.Div148 = state["Div148"]
		self.Div149 = state["Div149"]
		self.Flex29 = state["Flex29"]
		self.Div150 = state["Div150"]
		self.Div151 = state["Div151"]
		self.Flex30 = state["Flex30"]
		self.Div153 = state["Div153"]
		self.Div156 = state["Div156"]
		self.Flex81 = state["Flex81"]
		self.Flex82 = state["Flex82"]
		self.TextBox185 = state["TextBox185"]
		self.TextBox186 = state["TextBox186"]
		self.TextBox187 = state["TextBox187"]
		self.Image35 = state["Image35"]
		self.Image36 = state["Image36"]
		self.Image38 = state["Image38"]
		self.Image37 = state["Image37"]
		self.Image81 = state["Image81"]
		self.TextBox330 = state["TextBox330"]
		self.TextBox331 = state["TextBox331"]
		self.TextBox332 = state["TextBox332"]
		self.TextBox333 = state["TextBox333"]
		self.TextBox334 = state["TextBox334"]
		self.Image82 = state["Image82"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def Div307(self):
		self._getter_access_tracker["Div307"] = {}
		return self._Div307
	@Div307.setter
	def Div307(self, new_state):
		self._setter_access_tracker["Div307"] = {}
		global default_state
		self._Div307 = Div(new_state, default_state["Div307"])

	@property
	def Div147(self):
		self._getter_access_tracker["Div147"] = {}
		return self._Div147
	@Div147.setter
	def Div147(self, new_state):
		self._setter_access_tracker["Div147"] = {}
		global default_state
		self._Div147 = Div(new_state, default_state["Div147"])

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		global default_state
		self._Flex28 = Flex(new_state, default_state["Flex28"])

	@property
	def Div148(self):
		self._getter_access_tracker["Div148"] = {}
		return self._Div148
	@Div148.setter
	def Div148(self, new_state):
		self._setter_access_tracker["Div148"] = {}
		global default_state
		self._Div148 = Div(new_state, default_state["Div148"])

	@property
	def Div149(self):
		self._getter_access_tracker["Div149"] = {}
		return self._Div149
	@Div149.setter
	def Div149(self, new_state):
		self._setter_access_tracker["Div149"] = {}
		global default_state
		self._Div149 = Div(new_state, default_state["Div149"])

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		global default_state
		self._Flex29 = Flex(new_state, default_state["Flex29"])

	@property
	def Div150(self):
		self._getter_access_tracker["Div150"] = {}
		return self._Div150
	@Div150.setter
	def Div150(self, new_state):
		self._setter_access_tracker["Div150"] = {}
		global default_state
		self._Div150 = Div(new_state, default_state["Div150"])

	@property
	def Div151(self):
		self._getter_access_tracker["Div151"] = {}
		return self._Div151
	@Div151.setter
	def Div151(self, new_state):
		self._setter_access_tracker["Div151"] = {}
		global default_state
		self._Div151 = Div(new_state, default_state["Div151"])

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		global default_state
		self._Flex30 = Flex(new_state, default_state["Flex30"])

	@property
	def Div153(self):
		self._getter_access_tracker["Div153"] = {}
		return self._Div153
	@Div153.setter
	def Div153(self, new_state):
		self._setter_access_tracker["Div153"] = {}
		global default_state
		self._Div153 = Div(new_state, default_state["Div153"])

	@property
	def Div156(self):
		self._getter_access_tracker["Div156"] = {}
		return self._Div156
	@Div156.setter
	def Div156(self, new_state):
		self._setter_access_tracker["Div156"] = {}
		global default_state
		self._Div156 = Div(new_state, default_state["Div156"])

	@property
	def Flex81(self):
		self._getter_access_tracker["Flex81"] = {}
		return self._Flex81
	@Flex81.setter
	def Flex81(self, new_state):
		self._setter_access_tracker["Flex81"] = {}
		global default_state
		self._Flex81 = Flex(new_state, default_state["Flex81"])

	@property
	def Flex82(self):
		self._getter_access_tracker["Flex82"] = {}
		return self._Flex82
	@Flex82.setter
	def Flex82(self, new_state):
		self._setter_access_tracker["Flex82"] = {}
		global default_state
		self._Flex82 = Flex(new_state, default_state["Flex82"])

	@property
	def TextBox185(self):
		self._getter_access_tracker["TextBox185"] = {}
		return self._TextBox185
	@TextBox185.setter
	def TextBox185(self, new_state):
		self._setter_access_tracker["TextBox185"] = {}
		global default_state
		self._TextBox185 = TextBox(new_state, default_state["TextBox185"])

	@property
	def TextBox186(self):
		self._getter_access_tracker["TextBox186"] = {}
		return self._TextBox186
	@TextBox186.setter
	def TextBox186(self, new_state):
		self._setter_access_tracker["TextBox186"] = {}
		global default_state
		self._TextBox186 = TextBox(new_state, default_state["TextBox186"])

	@property
	def TextBox187(self):
		self._getter_access_tracker["TextBox187"] = {}
		return self._TextBox187
	@TextBox187.setter
	def TextBox187(self, new_state):
		self._setter_access_tracker["TextBox187"] = {}
		global default_state
		self._TextBox187 = TextBox(new_state, default_state["TextBox187"])

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		global default_state
		self._Image35 = Image(new_state, default_state["Image35"])

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		global default_state
		self._Image36 = Image(new_state, default_state["Image36"])

	@property
	def Image38(self):
		self._getter_access_tracker["Image38"] = {}
		return self._Image38
	@Image38.setter
	def Image38(self, new_state):
		self._setter_access_tracker["Image38"] = {}
		global default_state
		self._Image38 = Image(new_state, default_state["Image38"])

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		global default_state
		self._Image37 = Image(new_state, default_state["Image37"])

	@property
	def Image81(self):
		self._getter_access_tracker["Image81"] = {}
		return self._Image81
	@Image81.setter
	def Image81(self, new_state):
		self._setter_access_tracker["Image81"] = {}
		global default_state
		self._Image81 = Image(new_state, default_state["Image81"])

	@property
	def TextBox330(self):
		self._getter_access_tracker["TextBox330"] = {}
		return self._TextBox330
	@TextBox330.setter
	def TextBox330(self, new_state):
		self._setter_access_tracker["TextBox330"] = {}
		global default_state
		self._TextBox330 = TextBox(new_state, default_state["TextBox330"])

	@property
	def TextBox331(self):
		self._getter_access_tracker["TextBox331"] = {}
		return self._TextBox331
	@TextBox331.setter
	def TextBox331(self, new_state):
		self._setter_access_tracker["TextBox331"] = {}
		global default_state
		self._TextBox331 = TextBox(new_state, default_state["TextBox331"])

	@property
	def TextBox332(self):
		self._getter_access_tracker["TextBox332"] = {}
		return self._TextBox332
	@TextBox332.setter
	def TextBox332(self, new_state):
		self._setter_access_tracker["TextBox332"] = {}
		global default_state
		self._TextBox332 = TextBox(new_state, default_state["TextBox332"])

	@property
	def TextBox333(self):
		self._getter_access_tracker["TextBox333"] = {}
		return self._TextBox333
	@TextBox333.setter
	def TextBox333(self, new_state):
		self._setter_access_tracker["TextBox333"] = {}
		global default_state
		self._TextBox333 = TextBox(new_state, default_state["TextBox333"])

	@property
	def TextBox334(self):
		self._getter_access_tracker["TextBox334"] = {}
		return self._TextBox334
	@TextBox334.setter
	def TextBox334(self, new_state):
		self._setter_access_tracker["TextBox334"] = {}
		global default_state
		self._TextBox334 = TextBox(new_state, default_state["TextBox334"])

	@property
	def Image82(self):
		self._getter_access_tracker["Image82"] = {}
		return self._Image82
	@Image82.setter
	def Image82(self, new_state):
		self._setter_access_tracker["Image82"] = {}
		global default_state
		self._Image82 = Image(new_state, default_state["Image82"])

	def _to_json_fields(self):
		return {
			"Div307": self._Div307,
			"Div147": self._Div147,
			"Flex28": self._Flex28,
			"Div148": self._Div148,
			"Div149": self._Div149,
			"Flex29": self._Flex29,
			"Div150": self._Div150,
			"Div151": self._Div151,
			"Flex30": self._Flex30,
			"Div153": self._Div153,
			"Div156": self._Div156,
			"Flex81": self._Flex81,
			"Flex82": self._Flex82,
			"TextBox185": self._TextBox185,
			"TextBox186": self._TextBox186,
			"TextBox187": self._TextBox187,
			"Image35": self._Image35,
			"Image36": self._Image36,
			"Image38": self._Image38,
			"Image37": self._Image37,
			"Image81": self._Image81,
			"TextBox330": self._TextBox330,
			"TextBox331": self._TextBox331,
			"TextBox332": self._TextBox332,
			"TextBox333": self._TextBox333,
			"TextBox334": self._TextBox334,
			"Image82": self._Image82,
			}


class DivstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Div:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: DivstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = DivstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class FlexstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.flexDirection: str = get_defined_value(state, def_state, "flexDirection")
		self.alignItems: str = get_defined_value(state, def_state, "alignItems")
		self.justifyContent: str = get_defined_value(state, def_state, "justifyContent")
		self.flexWrap: str = get_defined_value(state, def_state, "flexWrap")
		self.alignContent: str = get_defined_value(state, def_state, "alignContent")
		self.rowGap: str = get_defined_value(state, def_state, "rowGap")
		self.columnGap: str = get_defined_value(state, def_state, "columnGap")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def flexDirection(self):
		self._getter_access_tracker["flexDirection"] = {}
		return self._flexDirection
	@flexDirection.setter
	def flexDirection(self, state):
		self._setter_access_tracker["flexDirection"] = {}
		self._flexDirection = state
	@property
	def alignItems(self):
		self._getter_access_tracker["alignItems"] = {}
		return self._alignItems
	@alignItems.setter
	def alignItems(self, state):
		self._setter_access_tracker["alignItems"] = {}
		self._alignItems = state
	@property
	def justifyContent(self):
		self._getter_access_tracker["justifyContent"] = {}
		return self._justifyContent
	@justifyContent.setter
	def justifyContent(self, state):
		self._setter_access_tracker["justifyContent"] = {}
		self._justifyContent = state
	@property
	def flexWrap(self):
		self._getter_access_tracker["flexWrap"] = {}
		return self._flexWrap
	@flexWrap.setter
	def flexWrap(self, state):
		self._setter_access_tracker["flexWrap"] = {}
		self._flexWrap = state
	@property
	def alignContent(self):
		self._getter_access_tracker["alignContent"] = {}
		return self._alignContent
	@alignContent.setter
	def alignContent(self, state):
		self._setter_access_tracker["alignContent"] = {}
		self._alignContent = state
	@property
	def rowGap(self):
		self._getter_access_tracker["rowGap"] = {}
		return self._rowGap
	@rowGap.setter
	def rowGap(self, state):
		self._setter_access_tracker["rowGap"] = {}
		self._rowGap = state
	@property
	def columnGap(self):
		self._getter_access_tracker["columnGap"] = {}
		return self._columnGap
	@columnGap.setter
	def columnGap(self, state):
		self._setter_access_tracker["columnGap"] = {}
		self._columnGap = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"flexDirection": self._flexDirection,
			"alignItems": self._alignItems,
			"justifyContent": self._justifyContent,
			"flexWrap": self._flexWrap,
			"alignContent": self._alignContent,
			"rowGap": self._rowGap,
			"columnGap": self._columnGap,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Flex:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: FlexstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = FlexstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class TextBoxstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class TextBoxcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class TextBox:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: TextBoxstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: TextBoxcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = TextBoxstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = TextBoxcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ImagestylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ImagecustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alt: str = get_defined_value(state, def_state, "alt")
		self.src: str = get_defined_value(state, def_state, "src")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alt(self):
		self._getter_access_tracker["alt"] = {}
		return self._alt
	@alt.setter
	def alt(self, state):
		self._setter_access_tracker["alt"] = {}
		self._alt = state
	@property
	def src(self):
		self._getter_access_tracker["src"] = {}
		return self._src
	@src.setter
	def src(self, state):
		self._setter_access_tracker["src"] = {}
		self._src = state
	def _to_json_fields(self):
		return {
			"alt": self._alt,
			"src": self._src,
			}


class Image:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ImagestylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ImagecustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ImagestylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ImagecustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

