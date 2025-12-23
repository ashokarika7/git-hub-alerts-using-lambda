#!/usr/bin/env python3

try:
    from main import app
    print("✅ App imported successfully")

    # Test OpenAPI schema generation
    schema = app.openapi()
    print("✅ OpenAPI schema generated successfully")

    info = schema.get('info', {})
    print(f"📖 API Title: {info.get('title')}")

    paths = schema.get('paths', {})
    print(f"📊 Paths available: {len(paths)}")

    # List all paths
    print("🛣️  Available endpoints:")
    for path in sorted(paths.keys()):
        methods = list(paths[path].keys())
        print(f"   {methods[0].upper()} {path}")

    print("\n🎉 App is ready for deployment!")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
