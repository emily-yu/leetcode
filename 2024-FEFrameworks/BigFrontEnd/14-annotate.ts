

import React, { useEffect, useRef } from 'react';


// referenced https://stackoverflow.com/a/63719707
// was unclear on return type operator (...) so referenced https://www.geeksforgeeks.org/what-do-these-three-dots-in-react-do/

export function useIsMounted(): () => boolean {
  // isMounted = false
  const isMounted = useRef(false) 

  useEffect(()=> {

    // set isMounted once running the setup function useEffect
    isMounted.current = true

    // when cleaning the function up, set this component instance's isMounted to false
    return () => {isMounted.current = false}
  })
  return () => isMounted.current
}


// to try your code on the right panel
// export App() component like below

// export function App() {
//   ...
//   return <div>BFE.dev</div>
// }


