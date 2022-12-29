import create from "zustand";

const useIoStore = create((set) => {
  return {
  "Home": {},
  "Services": {},
  "projects": {},
  "blog": {},
  "About": {},
  "education": {}
}});

export default useIoStore;
