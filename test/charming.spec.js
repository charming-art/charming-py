import { expect, test } from "vitest";
import * as cm from "./src/index.js";
import meta from "./package.json" assert { type: "json" };

for (const name of Object.keys(meta.dependencies)) {
  test(`@charming-art/charming should exports everything from ${name}`, async () => {
    const module = await import(name);
    for (const method of Object.keys(module)) {
      expect(cm[method]).toBe(module[method]);
    }
  });
}
