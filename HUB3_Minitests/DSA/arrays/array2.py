def process_elements(element)
#Example processing fundtion: squares the element. 
  return element **2
def capture_all_elements (array, batch_size = 10000):
    ###captures and process all elements in the array, handling large arrays efficiently.
    
    #Args:
    #array: list of elements to be processed
    #batch_size: Number of elements to process in each batch (for large arrays)

    for i in range(0, len(array), batch_size):
        batch = array[i:i + batch_size]
        try:
            processed_batch = [process_elements(el) for el in batch if element is not None]
            results.extend (processed_batch)
            print(f"Processed batch {i//batch_size + 1}: {len(processed_batch)} elements")
        except Exception as e:
            print(f"Error processing batch {i//batch_size + 1}: {e}")
            
            #verify all elements were processed correctly
    if len(results) != total_elements:
        print(f"Warning:Processed {len(results)}) element, expected {total_elements} elements")
    return results

  
